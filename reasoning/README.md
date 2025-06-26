

# AITL 推論層（Inference Layer）理論概要

## 概要

AITL（All-in-Theory Logic）における推論層は、  
**知識・観測・状態に基づいて行動を選択する中核的判断機構**です。  
論理・確率・最適化・自己修復の複数手法を統合し、**柔軟かつ信頼性の高い意思決定**を可能にします。

---

## 理論構成（全7章）

| ファイル | 内容概要 |
|----------|-----------|
| [`inference_layer.md`](./inference_layer.md) | 推論層の全体設計と4系統理論の統合フレームワーク |
| [`logic_reasoning.md`](./logic_reasoning.md) | 命題論理・述語論理による厳密推論。ルールベース制御に利用 |
| [`probabilistic_reasoning.md`](./probabilistic_reasoning.md) | ベイズ推論に基づく不確実性処理と状態信念更新 |
| [`mdp.md`](./mdp.md) | マルコフ決定過程による最適行動選択の数理基盤 |
| [`reinforcement_learning.md`](./reinforcement_learning.md) | 行動の学習と適応。モデルフリーな強化学習手法を記述 |
| [`self_repair.md`](./self_repair.md) | 故障診断・異常検出と動的修復判断の構造化理論 |
| [`graphical_models.md`](./graphical_models.md) | ベイズネット・因果グラフ等、確率構造をグラフで扱う補助理論 |

---

## 推論層の機能マップ
```
[センサ・観測]
↓
[推論層]
├── 論理推論（if-thenルール、命題記述）
├── 確率推論（Bayes, MAP, 尤度）
├── 最適化（MDP, 方策）
└── 自己修復（診断・代替・再学習）
↓
[制御層] → [物理層]
```
---

## 応用例（AITL-R / SkyEdge）

| シーン | 推論適用内容 |
|--------|--------------|
| センサ矛盾 | ベイズ推論 + 自己修復判断 |
| ドローン経路選択 | MDP + 強化学習による行動選択 |
| 故障復旧 | 自己修復 + 因果グラフで対処判断 |
| 状態評価 | 状態遷移と価値関数による最適化 |

---

## 実装との関係

推論層の理論は、実装層（`implementation/`）における次のモジュールに対応します：

- `inference_engine/`
- `reasoning_rules/`
- `belief_updater/`
- `diagnostic/`

AITLの設計思想として、**理論の透明性と実装の再利用性**を両立させるため、  
このドキュメント群は独立した理論リポジトリに位置づけています。

---

## 参考文献（総覧）

- Judea Pearl, *Causality*, 2009  
- Koller & Friedman, *Probabilistic Graphical Models*, 2009  
- Sutton & Barto, *Reinforcement Learning*, 2018  
- 三溝 真一, 『AITL推論理論概論』, 2025

---
