

# 確率推論（Probabilistic Reasoning）

## 概要

確率推論は、**不確実な情報を扱いながら推論・意思決定を行う**手法です。  
AITLでは、センサーデータの曖昧さ、状態の不完全観測、複数要因の因果関係を考慮するために、  
論理推論と並行して導入される重要な仕組みです。

---

## 基本構成

### ベイズの定理（Bayes' Theorem）

$$
P(H \mid D) = \frac{P(D \mid H) \cdot P(H)}{P(D)}
$$

- $( H $)：仮説（Hypothesis）  
- $( D $)：観測データ（Data）  
- $( P(H \mid D) $)：事後確率（Posterior）  
- $( P(D \mid H) $)：尤度（Likelihood）  
- $( P(H) $)：事前確率（Prior）  

---

## 推論の型

| 種類 | 内容 |
|------|------|
| ベイズ推定 | 観測に基づく事後分布の更新 |
| MAP推定（最大事後確率） | 最も確からしい仮説を選ぶ |
| MLE（最尤推定） | 観測を最もよく説明するパラメータを選ぶ |

---

## 条件付き確率と独立性

- $( P(A \mid B) = \frac{P(A \cap B)}{P(B)} $)  
- 独立なら $( P(A \cap B) = P(A) P(B) $)

---

## グラフィカルモデルとの関係

- ベイズネットワーク（DAG構造）で因果関係を明示  
- 推論アルゴリズム（Belief Propagation）と統合可能  
- 状態遷移やセンサの信頼度をモデリング

---

## AITLでの応用例

| 応用対象 | 内容 |
|----------|------|
| センサ融合 | センサAとBの信頼度に応じて統合出力を調整 |
| 故障診断 | 異常データの確率を推定し、閾値超えでアラート |
| 自己位置推定 | オドメトリ＋GPSの統合（Kalman Filter も含む） |

---

## 実装・手法

- ベイズ推定：逐次更新式でリアルタイム対応  
- ガウス分布・ベルヌーイ分布等の選択  
- サンプリング（MCMC）、近似（Variational Bayes）

---

## 限界と補完

- **モデル設計と事前分布の影響が大きい**  
- 高次元化により計算量が増加（→MCMC・粒子フィルタで緩和）  
- MDP・RLと組み合わせると**行動決定にも対応可能**

---

## 参考文献

- [1] Judea Pearl, *Probabilistic Reasoning in Intelligent Systems*, 1988  
- [2] Kevin Murphy, *Machine Learning: A Probabilistic Perspective*, 2012  
- [3] 三溝 真一, 『AITL推論理論概論』, 2025  

---


