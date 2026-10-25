"""Official notice classification, gov.cn parsing, and vigilance caps."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import official_notices as notices


def test_classify_keeps_rules_and_drops_company_recalls():
    assert notices.classify_title("国家药监局关于发布医疗器械出口销售证明管理规定的公告", strict=True) == "regulation_update"
    assert notices.classify_title("关于发布一次性使用输液器注册审查指导原则的通告", strict=True) == "guidance_new"
    assert notices.classify_title("46项医疗器械行业标准已经发布", strict=True) == "standard_revision"
    assert notices.classify_title("某公司主动召回输液泵一批", strict=True) is None
    assert notices.classify_title("医疗器械召回管理办法", strict=True) == "regulation_update"
    assert notices.classify_title("器审中心公开征求意见", strict=True) is None
    assert notices.classify_title("器审中心公开征求意见", strict=False) == "notice"


def test_parse_gov_policy_strips_markup_and_skips_drugs():
    payload = {
        "searchVO": {
            "listVO": [
                {
                    "title": "&lt;em&gt;国家药监局关于发布医疗器械出口销售证明管理规定的公告&lt;/em&gt;",
                    "url": "https://www.gov.cn/zhengce/zhengceku/202512/content_7052743.htm",
                    "pubtimeStr": "2025.12.25",
                    "puborg": "国家药监局",
                    "summary": "规范出口销售证明。",
                },
                {
                    "title": "国家药监局关于化学药品注册的公告",
                    "url": "https://www.gov.cn/zhengce/zhengceku/202511/content_1.htm",
                    "pubtimeStr": "2025.11.01",
                    "puborg": "国家药监局",
                    "summary": "",
                },
                {
                    "title": "某企业召回血糖仪",
                    "url": "https://www.gov.cn/zhengce/zhengceku/202510/content_2.htm",
                    "pubtimeStr": "2025.10.01",
                    "puborg": "国家药监局",
                    "summary": "",
                },
            ]
        }
    }
    items = notices.parse_gov_policy(payload)
    assert len(items) == 1
    assert items[0]["title"].startswith("国家药监局关于发布")
    assert items[0]["pub_date"] == "2025-12-25"
    assert items[0]["category_key"] == "nmpa/regulations"
    assert "<" not in items[0]["title"]


def test_first_sight_publishes_only_newest():
    entries = [{"title": f"公告{i}", "pub_date": f"2026-01-{i:02d}"} for i in range(1, 13)]
    chosen = notices.choose_unseen(entries, set(), baseline_limit=8)
    assert len(chosen) == 8
    again = notices.choose_unseen(entries, {item["title"] for item in entries})
    assert again == []
    fresh = notices.choose_unseen(entries + [{"title": "新公告", "pub_date": "2026-02-01"}], {item["title"] for item in entries})
    assert [item["title"] for item in fresh] == ["新公告"]


def test_vigilance_cap_keeps_newest_four():
    items = [{"title": str(i), "pub_date": f"2026-03-{i:02d}"} for i in range(1, 11)]
    capped = notices.cap_batch(items, "safety_communication")
    assert len(capped) == 4
    assert capped[0]["pub_date"] == "2026-03-10"
    regulatory = notices.cap_batch(items, "regulation_update")
    assert len(regulatory) == 10


def test_browser_inbox_rejects_foreign_links(tmp_path):
    path = tmp_path / "notices.json"
    path.write_text(json.dumps({
        "items": [
            {
                "title": "关于发布电子支气管镜注册审查指导原则的通告",
                "link": "https://www.cmde.org.cn/flfg/zdyz/a.html",
                "pub_date": "2026-09-18",
                "description": "全文",
                "source_name": "CMDE",
            },
            {
                "title": "Field safety notice for a ventilator",
                "link": "https://www.swissmedic.ch/fsca/1",
                "pub_date": "2026-09-18",
            },
        ]
    }), encoding="utf-8")
    items = notices.load_browser_inbox(path)
    assert len(items) == 1
    assert items[0]["category_key"] == "nmpa/guidance"
    assert items[0]["source_name"] == "CMDE"


def test_nmpa_job_no_longer_scrapes_the_blocked_page():
    import fetch_updates

    kinds = {item["check_type"] for item in fetch_updates.SOURCES["nmpa"].values()}
    assert kinds == {"gov_policy", "browser_inbox"}


def test_chinese_notice_titles_get_distinct_ids():
    import report_to_news

    first = report_to_news.generate_item_id("nmpa", "国家药监局关于发布医疗器械生产质量管理规范的公告", "2026-10-26")
    second = report_to_news.generate_item_id("nmpa", "国家药监局关于发布医疗器械网络销售质量管理规范的公告", "2026-10-26")
    assert first != second
    assert not first.endswith("_")
