
# マルコフ決定過程（Markov Decision Process, MDP）

## 概要

マルコフ決定過程（MDP）は、**確率的な状態遷移と報酬に基づく意思決定モデル**です。  
AITLでは、推論層において「どの状態で、どの行動を選ぶか」の評価を行い、  
最適な制御指示を生成するための数理的基盤として活用されます。

---

## 定義

MDPは5つの要素で構成されます：

$$
\mathcal{M} = (S, A, P, R, \gamma)
$$

| 要素 | 内容 |
|------|------|
| $( S $) | 状態空間（State space） |
| $( A $) | 行動空間（Action space） |
| $( P(s' \mid s, a) $) | 遷移確率（次状態） |
| $( R(s, a) $) | 即時報酬 |
| $( \gamma $) | 割引率（未来の報酬重視度） |

---

## 方策（Policy）と価値関数

- **方策**：状態に対して行動を選択するルール $( \pi(a \mid s) $)  
- **状態価値関数**：

$$
V^{\pi}(s) = \mathbb{E}_{\pi}\left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s \right]
$$

- **行動価値関数**：

$$
Q^{\pi}(s, a) = \mathbb{E}_{\pi}\left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s, a_0 = a \right]
$$

---

## 最適化とベルマン方程式

最適状態価値関数：

$$
V^*(s) = \max_a \left[ R(s,a) + \gamma \sum_{s'} P(s' \mid s,a) V^*(s') \right]
$$

⇒ **動的計画法**や**価値反復法（Value Iteration）**で計算可能
方策（Policy）と価値関数
	•	方策：状態に対して行動を選択するルール
$$
\pi(a \mid s)
$$
	•	状態価値関数：
$$
V^{\pi}(s) = \mathbb{E}{\pi}\left[ \sum{t=0}^{\infty} \gamma^t R(s_t, a_t) ,\middle|, s_0 = s \right]
$$
	•	行動価値関数：
$$
Q^{\pi}(s, a) = \mathbb{E}{\pi}\left[ \sum{t=0}^{\infty} \gamma^t R(s_t, a_t) ,\middle|, s_0 = s, a_0 = a \right]
$$

⸻

最適化とベルマン方程式
	•	最適状態価値関数（ベルマン最適方程式）：
$$
V^(s) = \max_a \left[ R(s,a) + \gamma \sum_{s’} P(s’ \mid s,a) V^(s’) \right]
$$
	•	⇒ 動的計画法や**価値反復法（Value Iteration）**で計算可能

---

## 部分観測MDP（POMDP）

- 状態 $( s $) を完全に観測できない場合の拡張モデル  
- 信念状態 $( b(s) $) によって確率的に推定しながら行動を選択

---

## AITLにおける応用

- 状態が曖昧な状況でも最適行動を導出  
- 推論層から「次に選ぶべきアクション」を制御層へ渡す  
- ドローンの航路選択、障害物回避、ミッション切り替えなどに有効

---

## 実装と応用手法

- Tabular MDP（状態数が小さい場合）  
- 関数近似による大規模MDP（Qネットワークなど）  
- POMDP Solver（e.g. SARSOP, Point-based methods）

---

## 参考文献

- [1] Martin L. Puterman, *Markov Decision Processes*, 1994  
- [2] Richard S. Sutton, Andrew Barto, *Reinforcement Learning*, 2018  
- [3] 三溝 真一, 『AITL推論理論概論』, 2025  

---

