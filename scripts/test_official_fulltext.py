"""gov.cn article extraction and catalog update decisions."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import official_fulltext as fulltext

PAGE = """
<html><body>
<div id="UCAP-CONTENT">
<p>国家药监局关于发布关节镜下无源手术器械产品等8项注册审查指导原则的通告（2021年第102号）</p>
<p>特此通告。</p>
<p>附件：<a href="./P020210001.doc">指导原则</a></p>
</div>
<a href="/unrelated.docx">页脚</a>
</body></html>
"""


def test_titles_and_section():
    notice = "国家药监局关于发布医疗器械出口销售证明管理规定的公告"
    assert fulltext.document_titles(notice) == ["医疗器械出口销售证明管理规定"]
    assert fulltext.target_section("医疗器械出口销售证明管理规定") == "nmpa/regulations"
    many = "关于发布《关节镜下无源手术器械产品注册审查指导原则》《麻醉面罩产品注册审查指导原则》的通告"
    assert fulltext.document_titles(many) == [
        "关节镜下无源手术器械产品注册审查指导原则",
        "麻醉面罩产品注册审查指导原则",
    ]
    assert fulltext.target_section("关节镜下无源手术器械产品注册审查指导原则") == "nmpa/guidance"


def test_parse_article_keeps_content_attachment_only():
    text, links = fulltext.parse_article(
        PAGE, "https://www.gov.cn/zhengce/zhengceku/2021-12/17/content_5661507.htm"
    )
    assert "特此通告" in text
    assert links == ["https://www.gov.cn/zhengce/zhengceku/2021-12/17/P020210001.doc"]
    assert fulltext.document_number(text) == "2021年第102号"


def test_plan_keeps_long_page_and_writes_missing_fulltext():
    long_page = {"body_len": 4000, "source_url": "https://reguverse.com/documentation/fsc/"}
    assert fulltext.plan_document(long_page, "甲" * 8000) == "retarget"
    official = {"body_len": 4000, "source_url": "https://www.gov.cn/zhengce/content.htm"}
    assert fulltext.plan_document(official, "甲" * 8000) == "present"
    assert fulltext.plan_document(None, "甲" * 800) == "create"
    assert fulltext.plan_document(None, "只有一段通告。") == "no_fulltext"
    short = {"body_len": 80, "source_url": ""}
    assert fulltext.plan_document(short, "甲" * 900) == "replace"


def test_split_numbered_attachments():
    body = (
        "附件1\n\n关节镜下无源手术器械产品\n\n注册审查指导原则\n\n"
        + ("甲" * 700)
        + "\n附件2\n\n麻醉面罩产品注册审查指导原则\n\n"
        + ("乙" * 700)
    )
    pieces = fulltext.split_attachments(body)
    assert [title for title, _ in pieces] == [
        "关节镜下无源手术器械产品注册审查指导原则",
        "麻醉面罩产品注册审查指导原则",
    ]


def test_split_named_documents():
    titles = ["关节镜下无源手术器械产品注册审查指导原则", "麻醉面罩产品注册审查指导原则"]
    body = titles[0] + ("甲" * 700) + "\n" + titles[1] + ("乙" * 700)
    chunks = fulltext.split_bodies(body, titles)
    assert set(chunks) == set(titles)
    assert chunks[titles[1]].startswith(titles[1])


def test_word_field_and_match():
    assert "I" in fulltext.clean_word_text("证明（ = 1 \\* ROMAN \\* MERGEFORMAT I）")
    pages = [{
        "key": fulltext.normalize_key("医疗器械出口销售证明管理规定"),
        "body_len": 20,
        "title": "医疗器械出口销售证明管理规定",
    }]
    found = fulltext.find_page(pages, "国家药监局关于发布医疗器械出口销售证明管理规定的公告")
    assert found["title"] == "医疗器械出口销售证明管理规定"
    edition = [{
        "title": "医疗器械生产质量管理规范(2025年版)",
        "body_len": 5000,
    }]
    assert fulltext.find_page(edition, "医疗器械生产质量管理规范", "2014年修订") is None
    assert fulltext.find_page(edition, "医疗器械生产质量管理规范", "自2025年11月起施行")["body_len"] == 5000
    editions = [
        {"title": "医疗器械生产质量管理规范（2014年版）", "body_len": 1000},
        {"title": "医疗器械生产质量管理规范(2025年版)", "body_len": 5000},
    ]
    assert fulltext.find_page(editions, "医疗器械生产质量管理规范", "第一条", "2025-11-06")["body_len"] == 5000
    assert fulltext.find_page(editions, "医疗器械生产质量管理规范", "第一条", "2014-12-01")["body_len"] == 1000
    notice = [{
        "title": "国家药监局关于进一步加强医疗器械注册人委托生产监督管理的公告（2024年第38号）",
        "body_len": 3000,
    }]
    assert fulltext.find_page(
        notice, "关于进一步加强医疗器械注册人委托生产监督管理", "", "2024-04-11"
    )["body_len"] == 3000


def test_render_page_has_catalog_fields():
    page = fulltext.render_page(
        doc_id="nmpa-gov-test",
        title="麻醉面罩产品注册审查指导原则",
        section="nmpa/guidance",
        doc_number="2021年第102号",
        source_url="https://www.gov.cn/zhengce/content.htm",
        attachment="https://www.gov.cn/a.doc",
        published="2021-12-17",
        body="第一条 适用范围。",
    )
    data, body = fulltext.split_front_matter(page)
    assert data["category"] == "nmpa/guidance"
    assert data["document_number"] == "2021年第102号"
    assert "第一条" in body
