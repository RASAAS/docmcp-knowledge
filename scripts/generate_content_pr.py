#!/usr/bin/env python3
"""
Generate bilingual Markdown content drafts and create a GitHub PR.

This script is triggered by the check-updates.yml workflow when regulatory
updates are detected. It:
1. Reads the update report from fetch_updates.py
2. Generates bilingual (EN + ZH) Markdown draft files for new/updated content
3. Commits the drafts to a new branch
4. Opens a GitHub PR for human review

Usage:
    python scripts/generate_content_pr.py --report update_report.json
    python scripts/generate_content_pr.py --report update_report.json --dry-run

Environment variables required (for PR creation):
    GITHUB_TOKEN   - GitHub personal access token with repo write access
    GITHUB_REPO    - Repository in owner/repo format (e.g. RASAAS/docmcp-knowledge)
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

ROOT = Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# Markdown template generators (bilingual EN + ZH)
# ---------------------------------------------------------------------------

def generate_eu_mdr_mdcg_draft(update: dict) -> tuple[str, str]:
    """Generate EN and ZH draft Markdown for a new MDCG guidance document."""
    name = update.get("name", "Unknown Source")
    url = update.get("url", "")
    category = update.get("category", "")
    detected_at = update.get("detected_at", datetime.now().isoformat())[:10]
    new_items = update.get("new_items", [])

    items_en = ""
    items_zh = ""
    for item in new_items[:5]:
        title = item.get("title", "")
        link = item.get("link", "")
        pub_date = item.get("pub_date", "")[:10] if item.get("pub_date") else ""
        if link:
            items_en += f"| [{title}]({link}) | {pub_date} |\n"
            items_zh += f"| [{title}]({link}) | {pub_date} |\n"
        else:
            items_en += f"| {title} | {pub_date} |\n"
            items_zh += f"| {title} | {pub_date} |\n"

    items_en_block = items_en if items_en else "| See source URL for details | - |\n"
    en_content = f"""---
title: MDCG Guidance Updates ({detected_at})
draft: true
source: {url}
detected_at: {detected_at}
---

# MDCG Guidance Updates

> **Draft**: Auto-generated from update detection. Requires human review before merging.

New or updated MDCG guidance documents detected from [{name}]({url}).

## Detected Updates

| Document | Date |
|----------|------|
{items_en_block}
::: tip Source
[EC — MDCG Endorsed Documents]({url})
:::

::: warning Review Required
This draft was auto-generated. Please verify content accuracy and update
the relevant docs pages (e.g., docs/en/eu_mdr/mdcg.md) before merging.
:::
"""

    items_zh_block = items_zh if items_zh else "| 请查看来源链接了解详情 | - |\n"
    zh_content = f"""---
title: MDCG 指南文件更新 ({detected_at})
draft: true
source: {url}
detected_at: {detected_at}
---

# MDCG 指南文件更新

> **草稿**：自动生成，合并前需人工审核。

从 [{name}]({url}) 检测到新的或更新的 MDCG 指南文件。

## 检测到的更新

| 文件 | 日期 |
|------|------|
{items_zh_block}
::: tip 来源
[欧盟委员会 — MDCG 文件]({url})
:::

::: warning 需要审核
此草稿为自动生成。请在合并前验证内容准确性，并更新相关文档页面
（如 docs/zh/eu_mdr/mdcg.md）。
:::
"""
    return en_content, zh_content


def generate_fda_guidance_draft(update: dict) -> tuple[str, str]:
    """Generate EN and ZH draft Markdown for FDA guidance updates."""
    name = update.get("name", "Unknown Source")
    url = update.get("url", "")
    detected_at = update.get("detected_at", datetime.now().isoformat())[:10]
    new_items = update.get("new_items", [])

    items_en = ""
    items_zh = ""
    for item in new_items[:10]:
        title = item.get("title", "")
        link = item.get("link", "")
        pub_date = item.get("pub_date", "")[:10] if item.get("pub_date") else ""
        if link:
            items_en += f"| [{title}]({link}) | {pub_date} |\n"
            items_zh += f"| [{title}]({link}) | {pub_date} |\n"
        else:
            items_en += f"| {title} | {pub_date} |\n"
            items_zh += f"| {title} | {pub_date} |\n"

    fallback_en = "| See source URL for details | - |\n"
    fallback_zh = "| 请查看来源链接了解详情 | - |\n"
    items_en_block = items_en if items_en else fallback_en
    items_zh_block = items_zh if items_zh else fallback_zh

    en_content = f"""---
title: FDA Guidance Updates ({detected_at})
draft: true
source: {url}
detected_at: {detected_at}
---

# FDA Guidance Updates

> **Draft**: Auto-generated from update detection. Requires human review before merging.

New FDA guidance documents detected from [{name}]({url}).

## Detected Updates

| Guidance | Date |
|----------|------|
{items_en_block}
::: tip Source
[FDA Standards Database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm)
:::

::: warning Review Required
This draft was auto-generated. Please verify content accuracy and update
the relevant docs pages (e.g., `docs/en/fda/guidance.md`) before merging.
:::
"""

    zh_content = f"""---
title: FDA 指导文件更新 ({detected_at})
draft: true
source: {url}
detected_at: {detected_at}
---

# FDA 指导文件更新

> **草稿**：自动生成，合并前需人工审核。

从 [{name}]({url}) 检测到新的 FDA 指导文件。

## 检测到的更新

| 指导文件 | 日期 |
|----------|------|
{items_zh_block}
::: tip 来源
[FDA 标准数据库](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm)
:::

::: warning 需要审核
此草稿为自动生成。请在合并前验证内容准确性，并更新相关文档页面
（如 `docs/zh/fda/guidance.md`）。
:::
"""
    return en_content, zh_content


def generate_nmpa_draft(update: dict) -> tuple[str, str]:
    """Generate EN and ZH draft Markdown for NMPA/CMDE updates."""
    name = update.get("name", "Unknown Source")
    url = update.get("url", "")
    detected_at = update.get("detected_at", datetime.now().isoformat())[:10]

    en_content = f"""---
title: NMPA/CMDE Updates ({detected_at})
draft: true
source: {url}
detected_at: {detected_at}
---

# NMPA/CMDE Regulatory Updates

> **Draft**: Auto-generated from update detection. Requires human review before merging.

Potential updates detected from [{name}]({url}).

::: tip Source
[CMDE Guidance Principles](https://www.cmde.org.cn/flfg/zdyz/)
:::

::: warning Review Required
This draft was auto-generated. Please manually check the source URL for new
guidance principles and update `docs/en/nmpa/guidance.md` accordingly.
:::
"""

    zh_content = f"""---
title: NMPA/CMDE 更新 ({detected_at})
draft: true
source: {url}
detected_at: {detected_at}
---

# NMPA/CMDE 法规更新

> **草稿**：自动生成，合并前需人工审核。

从 [{name}]({url}) 检测到潜在更新。

::: tip 来源
[CMDE 指导原则](https://www.cmde.org.cn/flfg/zdyz/)
:::

::: warning 需要审核
此草稿为自动生成。请手动检查来源 URL 中的新指导原则，
并相应更新 `docs/zh/nmpa/guidance.md`。
:::
"""
    return en_content, zh_content


def generate_generic_draft(update: dict) -> tuple[str, str]:
    """Generate a generic EN and ZH draft for any update type."""
    name = update.get("name", "Unknown Source")
    url = update.get("url", "")
    category = update.get("category", "unknown")
    detected_at = update.get("detected_at", datetime.now().isoformat())[:10]
    note = update.get("note", "")

    en_content = f"""---
title: Regulatory Update - {name} ({detected_at})
draft: true
source: {url}
category: {category}
detected_at: {detected_at}
---

# Regulatory Update: {name}

> **Draft**: Auto-generated from update detection. Requires human review before merging.

**Category**: `{category}`
**Source**: [{name}]({url})
**Detected**: {detected_at}
**Note**: {note}

::: warning Review Required
This draft was auto-generated. Please review the source URL and update
the relevant documentation pages before merging.
:::
"""

    zh_content = f"""---
title: 法规更新 - {name} ({detected_at})
draft: true
source: {url}
category: {category}
detected_at: {detected_at}
---

# 法规更新：{name}

> **草稿**：自动生成，合并前需人工审核。

**类别**：`{category}`
**来源**：[{name}]({url})
**检测时间**：{detected_at}
**说明**：{note}

::: warning 需要审核
此草稿为自动生成。请审核来源 URL 并在合并前更新相关文档页面。
:::
"""
    return en_content, zh_content


# ---------------------------------------------------------------------------
# Draft file path resolution
# ---------------------------------------------------------------------------

def get_draft_paths(update: dict, timestamp: str) -> tuple[Path, Path]:
    """Determine EN and ZH draft file paths based on update category."""
    category = update.get("category", "unknown")
    source_id = update.get("source_id", "update").replace("/", "_")
    slug = f"{source_id}_{timestamp}"

    drafts_dir = ROOT / "drafts"

    if category.startswith("eu_mdr/mdcg"):
        en_path = drafts_dir / "en" / "eu_mdr" / f"mdcg_{slug}.md"
        zh_path = drafts_dir / "zh" / "eu_mdr" / f"mdcg_{slug}.md"
    elif category.startswith("fda/guidance"):
        en_path = drafts_dir / "en" / "fda" / f"guidance_{slug}.md"
        zh_path = drafts_dir / "zh" / "fda" / f"guidance_{slug}.md"
    elif category.startswith("nmpa"):
        en_path = drafts_dir / "en" / "nmpa" / f"update_{slug}.md"
        zh_path = drafts_dir / "zh" / "nmpa" / f"update_{slug}.md"
    elif category.startswith("eu_mdr"):
        en_path = drafts_dir / "en" / "eu_mdr" / f"update_{slug}.md"
        zh_path = drafts_dir / "zh" / "eu_mdr" / f"update_{slug}.md"
    else:
        en_path = drafts_dir / "en" / f"update_{slug}.md"
        zh_path = drafts_dir / "zh" / f"update_{slug}.md"

    return en_path, zh_path


def select_generator(update: dict):
    """Select the appropriate content generator based on update category."""
    category = update.get("category", "")
    if "mdcg" in category:
        return generate_eu_mdr_mdcg_draft
    elif "fda/guidance" in category:
        return generate_fda_guidance_draft
    elif "nmpa" in category or "cmde" in category:
        return generate_nmpa_draft
    else:
        return generate_generic_draft


# ---------------------------------------------------------------------------
# Git operations
# ---------------------------------------------------------------------------

def run_git(args: list[str], cwd: Path = ROOT) -> tuple[int, str, str]:
    """Run a git command and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def create_branch(branch_name: str) -> bool:
    """Create and checkout a new git branch."""
    code, _, err = run_git(["checkout", "-b", branch_name])
    if code != 0:
        print(f"ERROR: Failed to create branch '{branch_name}': {err}")
        return False
    return True


def commit_files(files: list[Path], message: str) -> bool:
    """Stage and commit a list of files."""
    for f in files:
        code, _, err = run_git(["add", str(f)])
        if code != 0:
            print(f"ERROR: Failed to stage {f}: {err}")
            return False

    code, _, err = run_git(["commit", "-m", message])
    if code != 0:
        print(f"ERROR: Failed to commit: {err}")
        return False
    return True


def push_branch(branch_name: str) -> bool:
    """Push branch to origin."""
    code, _, err = run_git(["push", "origin", branch_name])
    if code != 0:
        print(f"ERROR: Failed to push branch: {err}")
        return False
    return True


# ---------------------------------------------------------------------------
# GitHub PR creation via API
# ---------------------------------------------------------------------------

def create_github_pr(
    branch_name: str,
    title: str,
    body: str,
    base: str = "main",
) -> Optional[str]:
    """Create a GitHub PR and return the PR URL."""
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPO", "RASAAS/docmcp-knowledge")

    if not token:
        print("WARNING: GITHUB_TOKEN not set. Skipping PR creation.")
        return None

    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    payload = {
        "title": title,
        "body": body,
        "head": branch_name,
        "base": base,
        "draft": True,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code == 201:
            pr_url = resp.json().get("html_url", "")
            print(f"PR created: {pr_url}")
            return pr_url
        else:
            print(f"ERROR: GitHub API returned {resp.status_code}: {resp.text[:200]}")
            return None
    except Exception as e:
        print(f"ERROR: Failed to create PR: {e}")
        return None


# ---------------------------------------------------------------------------
# Main workflow
# ---------------------------------------------------------------------------

def process_updates(report: dict, dry_run: bool = False) -> int:
    """Process update report and generate draft PRs. Returns number of PRs created."""
    updates = report.get("updates", [])
    if not updates:
        print("No updates to process.")
        return 0

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    branch_name = f"auto/content-updates-{timestamp}"
    generated_files: list[Path] = []
    pr_body_sections: list[str] = []

    print(f"\nProcessing {len(updates)} update(s)...")

    for update in updates:
        source_id = update.get("source_id", "unknown")
        name = update.get("name", "Unknown")
        category = update.get("category", "")
        print(f"\n  [{category}] {name}")

        generator = select_generator(update)
        en_content, zh_content = generator(update)
        en_path, zh_path = get_draft_paths(update, timestamp)

        if dry_run:
            print(f"    [DRY RUN] Would create: {en_path.relative_to(ROOT)}")
            print(f"    [DRY RUN] Would create: {zh_path.relative_to(ROOT)}")
        else:
            en_path.parent.mkdir(parents=True, exist_ok=True)
            zh_path.parent.mkdir(parents=True, exist_ok=True)
            en_path.write_text(en_content, encoding="utf-8")
            zh_path.write_text(zh_content, encoding="utf-8")
            generated_files.extend([en_path, zh_path])
            print(f"    Created: {en_path.relative_to(ROOT)}")
            print(f"    Created: {zh_path.relative_to(ROOT)}")

        pr_body_sections.append(
            f"- **[{category}]** {name}\n"
            f"  - Source: {update.get('url', '')}\n"
            f"  - Note: {update.get('note', 'Manual review required')}"
        )

    if dry_run:
        print(f"\n[DRY RUN] Would create branch: {branch_name}")
        print(f"[DRY RUN] Would commit {len(updates) * 2} draft files")
        print(f"[DRY RUN] Would open PR: 'chore: auto-detected regulatory updates {timestamp}'")
        return len(updates)

    if not generated_files:
        print("No files generated.")
        return 0

    # Create branch and commit
    print(f"\nCreating branch: {branch_name}")
    if not create_branch(branch_name):
        return 0

    commit_msg = f"chore: auto-detected regulatory content drafts ({timestamp})\n\nGenerated by generate_content_pr.py"
    if not commit_files(generated_files, commit_msg):
        return 0

    # Push branch
    print(f"Pushing branch...")
    if not push_branch(branch_name):
        return 0

    # Create PR
    pr_title = f"[Auto] Regulatory content updates detected ({timestamp})"
    pr_body = f"""## Auto-detected Regulatory Updates

This PR was automatically generated by `scripts/generate_content_pr.py` after
`scripts/fetch_updates.py` detected potential changes in official regulatory sources.

**Detected updates ({len(updates)}):**

{chr(10).join(pr_body_sections)}

## Review Instructions

1. Review each draft file in the `drafts/` directory
2. Update the corresponding `docs/en/` and `docs/zh/` pages with verified content
3. Delete the draft files after incorporating their content
4. Run `python scripts/verify_urls.py --docs` to validate all links
5. Merge when content is verified

> **Note**: Draft files are in `drafts/` and are NOT rendered by VitePress.
> They are for review purposes only.
"""

    pr_url = create_github_pr(branch_name, pr_title, pr_body)
    if pr_url:
        print(f"\nPR opened: {pr_url}")
    else:
        print(f"\nBranch pushed but PR creation skipped (no GITHUB_TOKEN).")
        print(f"Create PR manually from branch: {branch_name}")

    return len(updates)


def main():
    parser = argparse.ArgumentParser(
        description="Generate bilingual content drafts and create PR from update report"
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Path to update report JSON from fetch_updates.py --report",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without creating files or PRs",
    )
    parser.add_argument(
        "--base-branch",
        default="main",
        help="Base branch for the PR (default: main)",
    )
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f"ERROR: Report file not found: {report_path}")
        sys.exit(1)

    try:
        with open(report_path, "r", encoding="utf-8") as f:
            report = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to read report: {e}")
        sys.exit(1)

    updates_found = report.get("updates_found", 0)
    if updates_found == 0:
        print("No updates in report. Nothing to do.")
        sys.exit(0)

    print(f"Report: {report.get('summary', '')}")
    print(f"Updates: {updates_found}")

    count = process_updates(report, dry_run=args.dry_run)
    print(f"\nDone. Processed {count} update(s).")


if __name__ == "__main__":
    main()
