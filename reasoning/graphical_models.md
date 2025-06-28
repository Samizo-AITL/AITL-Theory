

# グラフィカルモデル（Graphical Models）

## 概要

グラフィカルモデルは、**変数間の確率的・因果的関係をグラフ構造で表現する手法**です。  
AITLにおいては、状態の依存構造や因果連鎖、推論の効率化に不可欠な概念であり、  
確率推論・自己修復推論と密接に連携します。

---

## 種類と構成

### 1. ベイズネットワーク（Bayesian Network）

- 有向非巡回グラフ（DAG）で構成  
- ノード：確率変数  
- 辺：因果・依存関係（親→子）  
- 各ノードは条件付き確率表（CPT）で定義

例：
```
Battery → Sensor → Diagnosis
↓
Motor
```
$$
P(A, B, C) = P(A) \cdot P(B \mid A) \cdot P(C \mid B)
$$

---

### 2. マルコフネットワーク（Markov Random Field）

- 無向グラフ  
- エネルギー関数またはポテンシャル関数で表現  
- 局所的な相互依存性（近傍）を重視

---

## 推論アルゴリズム

| 手法 | 内容 |
|------|------|
| Belief Propagation | メッセージ伝播で周辺確率を計算（ツリー構造で正確） |
| Variable Elimination | 関係変数を順に統合し周辺化 |
| MCMC（サンプリング） | 高次元の場合に確率分布を近似生成 |

---

## AITLにおける応用

- **センサ間の依存関係構築**（例：センサAがBに影響を与える）  
- **故障診断の因果推論**（ノードの事後確率変化による異常源推定）  
- **行動決定の条件付き評価**（複数因子を統合して最良アクション選択）

---

## 形式的定義（ベイズネット）

- ノード集合 $( X = \{X_1, X_2, ..., X_n\} $)  
- 有向辺集合 $( E $)  
- 条件付き確率分布：

$$
P(X_1, ..., X_n) = \prod_{i=1}^n P(X_i \mid Pa(X_i))
$$

ここで $( Pa(X_i) $) は $( X_i $) の親ノード集合

---

## 実装・ツール例

- Pythonライブラリ：`pgmpy`, `BayesPy`, `Pyro`  
- 可視化：`Graphviz`, `networkx`, `Gephi`  
- 設計：ノード構造と依存関係をDSL/JSON-LDで記述

---

## AITLとの接続

- **probabilistic_reasoning.md**：ベイズ推論の構造化拡張  
- **self_repair.md**：故障診断グラフの基盤  
- **inference_engine**：状態更新と原因帰属に利用

---

## 参考文献

- [1] Daphne Koller & Nir Friedman, *Probabilistic Graphical Models*, 2009  
- [2] Judea Pearl, *Causality*, 2009  
- [3] 三溝 真一, 『AITL推論理論概論』, 2025  

---

