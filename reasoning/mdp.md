# マルコフ決定過程（Markov Decision Process, MDP）

## 概要

マルコフ決定過程（MDP）は、**確率的な状態遷移と報酬に基づく意思決定モデル**です。  
AITLにおいては、推論層で「どの状態で、どの行動を選ぶか」を数理的に評価し、  
最適な制御指示を生成するための基盤理論として活用されます。

---

## 定義

MDPは、以下の5つの要素によって定義されます：

$$
\mathcal{M} = (S, A, P, R, \gamma)
$$

| 要素 | 内容 |
|------|------|
| $S$ | 状態空間（State space） |
| $A$ | 行動空間（Action space） |
| $P(s' \mid s, a)$ | 状態遷移確率（次状態 $s'$ への遷移確率） |
| $R(s, a)$ | 即時報酬関数（行動 $a$ を取ったときの報酬） |
| $\gamma$ | 割引率（将来の報酬に対する重み，$0 \leq \gamma < 1$） |

---

## 方策（Policy）と価値関数

**方策**とは、各状態 $s$ において行動 $a$ を選択する確率的ルール：

$$
\pi(a \mid s)
$$

### 状態価値関数（State Value Function）：

ある方策 $\pi$ の下で状態 $s$ にいるときの期待される累積報酬：

$$
V^{\pi}(s) = \mathbb{E}_{\pi}\left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \,\middle|\, s_0 = s \right]
$$

### 行動価値関数（Action Value Function）：

状態 $s$ で行動 $a$ をとったときの期待累積報酬：

$$
Q^{\pi}(s, a) = \mathbb{E}_{\pi}\left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \,\middle|\, s_0 = s, a_0 = a \right]
$$

---

## 最適化とベルマン方程式

最適状態価値関数 $V^*(s)$ は以下の**ベルマン最適方程式**を満たします：

$$
V^*(s) = \max_{a} \left[ R(s, a) + \gamma \sum_{s'} P(s' \mid s, a) V^*(s') \right]
$$

これにより、**動的計画法**や**価値反復法（Value Iteration）**などで逐次的に最適解を導出できます。

---

## 部分観測MDP（POMDP）

実環境では、状態 $s$ を完全には観測できない場合が多く、  
そのような状況に対処するための拡張が**部分観測MDP（POMDP）**です。

- **信念状態（Belief State）**：$b(s)$  
  状態 $s$ にあると信じる確率分布（確率的推定）

POMDPでは、この信念状態に基づいて方策 $\pi(a \mid b)$ を定義し、  
不完全情報下でも意思決定を行います。

---

## AITLにおける応用

AITL推論層では、MDP/POMDPの枠組みに基づいて以下を実現します：

- 状態遷移や環境不確実性を含む状況下での最適行動選択  
- 推論層が導出したアクションを制御層へ受け渡し、実行へ反映  
- ドローンの経路選定、障害物回避、マルチミッションの切り替えなどに適用

---

## 実装と応用手法

| 手法 | 概要 |
|------|------|
| Tabular MDP | 状態・行動空間が小さい場合の表形式実装 |
| 関数近似 | ニューラルネットなどによる大規模空間のQ関数近似（例：DQN） |
| POMDP Solver | SARSOP、Point-based Value Iteration などの近似解法 |

---

## 参考文献

- [1] Martin L. Puterman, *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, 1994  
- [2] Richard S. Sutton, Andrew G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., 2018  
- [3] 三溝 真一, 『AITL推論理論概論』, 2025  
