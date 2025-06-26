
# 論理推論（Logical Reasoning）

## 概要

論理推論は、**明示的なルールと前提知識**に基づいて結論を導く形式的手法です。  
AITLでは、状態の意味づけ、目標生成、条件付きアクションの選択などに使われ、  
推論層の**中核的な判断エンジン**を構成します。

---

## 推論の基本構造

### 命題論理（Propositional Logic）

- 事実を真理値（True/False）で表現  
- 演算：AND (∧), OR (∨), NOT (¬), 含意 (→) など

例：
```
A → B （Aが成り立てばBも成り立つ）
A
∴ B（Modus Ponensによって導かれる結論）
```

### 述語論理（Predicate Logic）

- 対象に関する性質や関係を表現可能  
- \( P(x), Q(x, y) \) のような構文  
- 全称記号 ∀、存在記号 ∃ などを用いる

例：
```
∀x Animal(x) → Mortal(x)
Animal(Socrates)
∴ Mortal(Socrates)
```
---

## 推論規則と手法

| 規則 | 説明 |
|------|------|
| Modus Ponens | A → B, A より B を導く |
| Modus Tollens | A → B, ¬B より ¬A を導く |
| 合取導入 | A, B より A∧B を導く |
| 否定導出法 | 仮定と矛盾から否定を導く |

---

## 真理値表（Truth Table）

| A | B | A∧B | A∨B | A→B |
|---|---|-----|-----|------|
| T | T |  T  |  T  |  T   |
| T | F |  F  |  T  |  F   |
| F | T |  F  |  T  |  T   |
| F | F |  F  |  F  |  T   |

---

## AITLにおける応用例

- 「バッテリー低下」→「充電行動へ移行」  
- 「センサAとBが不一致」→「診断モードに遷移」  
- 「∀x (障害物(x) → 回避動作(x))」による自律回避

---

## 実装観点

- 論理ルールベースの推論エンジン（例：Prolog、Z3）  
- AITLではJSON-LDや内部DSL形式で表現し、他層と接続可能  
- 状態変数・目標・制約の**意味付け・整合性確認**に有効

---

## 限界と補完理論

- 完全性は高いが、**不確実性には弱い**  
- ベイズ推論やMDPとの**補完統合**が重要（→別ファイル参照）

---

## 参考文献

- [1] Patrick Blackburn et al., *Logic and Models of Reasoning*, 2011  
- [2] Stuart Russell, Peter Norvig, *Artificial Intelligence*, 2020  
- [3] 三溝 真一, 『AITL推論理論概論』, 2025  

---
