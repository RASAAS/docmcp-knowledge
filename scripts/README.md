# Scripts / 工具脚本

## 脚本说明

| 脚本 | 功能 |
|------|------|
| `migrate_wordpress.py` | 从 WordPress REST API 批量导出内容并转换为 Markdown |
| `validate_schema.py` | 验证 JSON 元数据是否符合 schemas/ 中的 schema |
| `verify_urls.py` | 验证所有来源 URL 的有效性 |
| `fetch_updates.py` | 自动检查各官方源的更新，创建 PR 草稿 |

## 安装依赖 / Install Dependencies

```bash
pip install requests html2text python-docx pyyaml jsonschema
```

## 使用示例 / Usage

```bash
# 验证所有 JSON 元数据
python scripts/validate_schema.py

# 验证单个文件的 URL
python scripts/verify_urls.py --file nmpa/guidance/21-sw/cmde-2022-9.zh.md

# 验证所有 URL
python scripts/verify_urls.py --all

# 从 WordPress 迁移内容
python scripts/migrate_wordpress.py --site https://reguverse.com --post-type docs --output ./
```
