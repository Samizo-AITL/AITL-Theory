

# 強化学習（Reinforcement Learning, RL）

## 概要

強化学習は、**環境との相互作用を通じて報酬を最大化するような方策（Policy）を学習する手法**です。  
AITLでは、未知環境下での自律的な適応・最適行動選択・継続的な学習に応用されます。

---

## 基本構造

強化学習は以下の要素で構成されます：

| 要素 | 内容 |
|------|------|
| 環境（Environment） | 状態遷移と報酬を定義するシステム |
| エージェント（Agent） | 行動を選択し報酬を受け取る学習主体 |
| 状態 \$$( s \$$) | 現在の環境情報 |
| 行動 \$$( a \$$) | エージェントの選択可能な操作 |
| 報酬 \$$( r \$$) | 行動の評価スカラー |
| 方策 \$$( \pi(a \mid s) \$$) | 行動の選択確率 |

---

## 代表的手法

### 1. Q学習（Q-learning）

- オフポリシー型の価値ベース学習

\$$
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]
\$$

- テーブル型または関数近似で実装可能

---

### 2. SARSA

- オンポリシー型：実際に選んだ行動に基づいて更新

\$$
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma Q(s', a') - Q(s, a)]
\$$

---

### 3. 方策勾配法（Policy Gradient）

- 方策自体を直接最適化：

\$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} [\nabla_\theta \log \pi_\theta(a \mid s) Q^\pi(s, a)]

\$$

- Actor-Critic法、PPO（Proximal Policy Optimization）などに発展

---

## 探索と活用（Exploration vs Exploitation）

- ε-greedy戦略：確率 ε でランダム行動、1-ε で最良行動  
- Softmax方式やUCB（Upper Confidence Bound）も有効

---

## AITLでの応用

- **環境変化に適応可能な動作学習**（例：障害物が変化するドローン経路）  
- **モデルフリー制御**：物理層モデルが不明な場合でも学習可能  
- **自己修復戦略の再学習**（例：新たな障害条件への動的対応）

---

## 実装上の考慮点

- 状態空間・行動空間の次元削減（状態特徴抽出）  
- 遅延報酬（Delayed reward）の取り扱い  
- エピソード設計と報酬設計の工夫

---

## 関連モデル

- MDP（理論的土台） → `mdp.md` 参照  
- POMDPベースのRL（観測が不完全な状況下での学習）  
- メタ学習・継続学習と連携可能

---

## 参考文献

- [1] Sutton & Barto, *Reinforcement Learning: An Introduction*, 2018  
- [2] Richard S. Sutton, *Policy Gradient Methods for RL with Function Approximation*, 2000  
- [3] 三溝 真一, 『AITL推論理論概論』, 2025  

---
