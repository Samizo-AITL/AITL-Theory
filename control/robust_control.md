
# ロバスト制御（Robust Control）

## 概要

頑健制御は、システムのモデル誤差や外乱に対して、  
**性能劣化を最小限に抑えつつ安定性を保証する制御手法**です。  
AITLでは、不確実性のある環境や構成部品のばらつきを考慮し、  
信頼性の高い制御を実現するために採用されます。

---

## 基本概念

- モデル不確かさ（パラメータ変動、外乱）を明示的に扱う  
- 制御系の閉ループ安定性をロバストに保つ  
- 性能指標（H∞ノルム、μ解析など）を用いた評価・設計

---

## 代表的手法

### 1. H∞制御

- 周波数領域でのノルム最小化問題として設計  
- 外乱に対する最大ゲインを抑制し、安定性を確保

### 2. μ合成

- 不確かさモデルの詳細な扱いにより最適制御器設計  
- 複雑な不確実性を含むシステムにも適用可能

### 3. スライディングモード制御

- 不連続制御入力により頑健性を実現  
- モデル誤差や外乱に強いが、チャタリング現象に注意

---

## 数理モデル例

一般的なロバスト制御問題は次のように表現される：

$$
\min_K \| T_{zw}(s) \|_{\infty}
$$

ここで $( T_{zw}(s) $) は外乱入力 $( w $) から制御出力 $( z $) への伝達関数行列、  
$( \| \cdot \|_{\infty}$) はH∞ノルム。

---

## AITLでの応用例

- 変動する環境下のドローン制御  
- 部品劣化を考慮したロボットの長期安定動作  
- 外乱耐性を必要とするインクジェット制御

---

## 実装上のポイント

- モデル不確実性の定式化と評価  
- 計算負荷とリアルタイム性能のバランス  
- 調整パラメータの解釈と設定

---

## 参考文献

- Zhou, Doyle, Glover, *Robust and Optimal Control*, 1996  
- Skogestad & Postlethwaite, *Multivariable Feedback Control*, 2005  
- 三溝 真一, 『AITL制御論概論』, 2025

---


