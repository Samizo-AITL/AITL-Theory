# AITL - All-in-Theory Logic 理論コア  
(Core Theory of All-in-Theory Logic Architecture)

---

## 概要 / Overview

**AITL（All-in-Theory Logic）** は、次世代AIシステムのための**完全理論ベースの階層アーキテクチャ**です。  
本ディレクトリは、AITLの中核をなす **理論構造（v1.0）** をまとめています。

---

## Versioning and Role of This Directory  
バージョン体系と本ディレクトリの役割

AITLは統一アーキテクチャとして進化し、その段階をバージョンで示します。

| バージョン名               | 内容（日本語）                                                                 | 内容（英語）                                                                 |
|----------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **AITL v1.0 (Theory only)** | 推論・制御・物理の三層理論モデルを抽象的に定義した理論コア。                 | Abstract core theory defining the three-layer model: Logic, Control, Physical. |
| **AITL v2.0 (Theory + Impl.)** | v1.0の理論を基に具体的な実装・応用を加えた拡張版。                           | Extended version adding concrete implementations and applications based on v1.0 theory. |

🧠 **本リポジトリは「AITL v1.0 (Theory only)」を扱います。**  
v2.0は理論を包含しつつ、実装と応用に拡張された段階です。

---

## AITLの三層構造 / Three-layer Architecture of AITL

AITLは以下の **三層構造** を持ちます：

```
┌──────────────┐
│ Logic Layer  │ ← 状態認識、因果推論、自己修復などの推論機能
├──────────────┤
│ Control Layer│ ← MPC / PID / ロバスト制御による信号生成
├──────────────┤
│ Physical Layer│ ← センサノイズ・動力学・外乱の物理モデリング
└──────────────┘
```

| 層（日本語）     | Layer (English) | 説明 / Description |
|------------------|------------------|---------------------|
| **推論層**        | Logic Layer      | 状態認識、制約推論、目標生成、自己修復などの論理的推論を担当。論理プログラミングや因果推論も含む。<br>Responsible for logical inference, state recognition, constraint reasoning, goal generation, and self-repair logic. Includes logic programming and causal inference. |
| **制御層**        | Control Layer    | 推論層の出力を基に制御信号を生成。MPC、PID制御、ロバスト制御などを用いる。<br>Generates control signals based on logic layer output, employing MPC, PID, and robust control methods. |
| **物理層**        | Physical Layer   | ロボットやドローンの物理動力学、センサノイズ、外乱をモデル化。<br>Models physical dynamics, sensor noise, and disturbances of real-world systems. |

---

## 理論と実装の関係性  
Relationship Between Theory and Implementation

- **AITLの理論（v1.0）**は独立した「設計図」であり、  
- これを基に応用・実装が **v2.0** へと発展しています。

理論と実装は「分離」ではなく、  
理論を内包した「**進化のステージ**」として連続性を持ちます。

---

## 応用例（v2.0のイメージ）  
Examples of v2.0 Implementations

| プロジェクト名（日本語） | Project Name (English) | 概要 / Description |
|--------------------------|-------------------------|---------------------|
| **AITL-R**               | AITL-R                  | ロボット向けの障害推論・冗長制御などを含む実装例。<br>Robotic implementation including fault inference and redundancy control. |
| **SkyEdge**              | SkyEdge                 | ドローン飛行制御と自己修復判断を実装。<br>Drone flight control and self-repair decision making. |
| **OpenSim-AITL**         | OpenSim-AITL            | 物理層モデリングと強化学習の統合シミュレーション。<br>Simulation integrating physical modeling and reinforcement learning. |

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](../LICENSE) file for details.

---

## Author

**Shinichi Samizo（三溝 真一）**  
Creator and lead theorist of the AITL framework.

---

## Contact

ご質問やフィードバックは Issue またはメールでお気軽にどうぞ。  
Feel free to reach out via GitHub Issues or email.
