<script type="text/javascript"
  id="MathJax-script"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# モデル予測制御（Model Predictive Control, MPC）

## 概要

モデル予測制御（MPC）は、**未来の状態を予測し、最適な制御入力を逐次決定する**手法です。  
AITLでは、論理推論から導かれる目標や制約を受け、物理層の状態に基づき**最適な動作計画を制御出力へ変換**する役割を担います。

---

## 基本概念

- 制御対象の**動的モデル**を用いて、将来の状態を予測
- **一定の時間地平（horizon）**内で最適な入力列を計算
- 実行は**直近1ステップ分**のみで、次ステップで再計算（逐次最適化）

---

## 数式モデル（離散時間）

状態方程式と出力方程式：

\[
x_{k+1} = A x_k + B u_k
\]
\[
y_k = C x_k + D u_k
\]

最適化問題：

\[
\min_{\{u_k\}} \sum_{i=0}^{N} \left( x_{k+i}^T Q x_{k+i} + u_{k+i}^T R u_{k+i} \right)
\]
\[
\text{subject to: } x_{k+i+1} = A x_{k+i} + B u_{k+i}, \quad x_{k+i} \in \mathcal{X}, \quad u_{k+i} \in \mathcal{U}
\]

---

## 特徴と利点

- **制約条件**（操作量・状態の範囲）を明示的に扱える  
- **マルチステップ先読み**で安定性と安全性を確保  
- 非線形拡張（NMPC）も可能

---

## 実装上の注意点

- 計算コストが高く、**リアルタイム性確保には工夫が必要**  
- **モデル精度**が性能に強く影響（状態空間モデルの整備が前提）  
- ソルバー選定（QP, SQP, CasADi など）が性能を左右

---

## AITLにおけるMPCの活用

- 推論層で生成された**意図・制約・状態評価**を取り込み、制御入力へ変換  
- ドローンの**飛行経路追従**（SkyEdge）  
- 状況変化に応じた**自律的行動の切り替え**（AITL-R）

---

## 応用例

| 応用対象 | 内容 |
|----------|------|
| ドローン | 経路最適化、風対応姿勢補正 |
| インクジェット | 多パラメータ制御（波形×温度×圧力） |
| 自動運転 | 軌道計画＋障害物回避制御 |

---

## 参考文献

- [1] A. Bemporad et al., “Model Predictive Control: Theory and Applications”, 2002  
- [2] K.J. Åström, *Feedback Systems*, 2008  
- [3] 三溝 真一, 『AITL制御論概論』, 2025  

---
