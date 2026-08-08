# GSPR 合规清单（IVDR）

**IVDR 参考：** 附件一（一般安全与性能要求）  
**BPG 参考：** Team-NB BPG-IVDR V2（约第 15 页）  
**文件代码：** AII-S4

## 清单结构要求

- [ ] 对附件一 **每一条**适用 GSPR 给出符合性论证；含分节的 GSPR 须**独立**处理各分节
- [ ] 明确每条适用 GSPR 的符合性证明方法（标准、CS、其他方法、内部规范等）
- [ ] 精确标识证明符合性的受控文件（文件名/编号/版本/日期），并交叉引用其在完整 TD 中的位置
- [ ] 适用标准与 CS 列表；部分采用或偏离时提供摘要/差距分析与正当理由
- [ ] 不适用 GSPR：给出不适用理由（与预期用途/技术特征一致）

## 建议列（示例）

| GSPR | 适用? | 符合方法 | 适用标准/CS | 证据文件位置 | 备注 |
|------|-------|----------|-------------|--------------|------|
| … | Y/N | … | … | … | … |

## 证据邻居（IVDR）

- [ ] 证据指向 **PER / 分析性能 / 临床性能 / RM / V&V / 标签 IFU**，而非 MDR CER
- [ ] Applied Standards 与 Complying Documents 按 IVD 语境填写（含性能评价相关）

## Reguverse 工作流提示

- 使用 `eu_ivdr` 的 Annex I 全文数据生成 checklist（条款号为 IVDR）
- 勿混用 MDR GSPR 编号

## 相关页面

- [风险管理](./risk-management)
- [性能评价](./performance-evaluation)
- [产品验证与确认](./verification-validation)
