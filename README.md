# AITL v1.0 - Core Theory of All-in-Theory Logic Architecture  
（AITL理論アーキテクチャ中核：完全理論モデル）

---

## 概要 / Overview

**AITL（All-in-Theory Logic）** は、ロボティクスや自律エージェントのための  
**推論・制御・物理モデリング**を統合した**完全理論ベースの階層アーキテクチャ**です。  
本ディレクトリでは、AITLの中核となる **理論構造（v1.0）** を定義します。

---

## バージョン体系と本ディレクトリの役割  
Versioning and Role of This Directory

AITLは進化するアーキテクチャであり、以下のバージョン体系を持ちます：

| バージョン名               | 内容（日本語）                                                                 | 内容（英語）                                                                 |
|----------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **AITL v1.0 (Theory only)** | 推論・制御・物理の三層理論モデルを抽象的に定義した理論コア。                 | Abstract core theory defining the three-layer model: Logic, Control, Physical. |
| **AITL v2.0 (Theory + Impl.)** | v1.0の理論を基に具体的な実装・応用を加えた拡張版。                           | Extended version adding concrete implementations and applications based on v1.0 theory. |

🧠 **本ディレクトリは「AITL v1.0 (Theory only)」に対応します。**  
v2.0は、v1.0の理論を内包しつつ応用・実装に拡張した進化形です。  
※理論と実装は分離された段階ではなく、**理論を内包する進化のステージ**です。

---

## AITLの三層構造 / Three-layer Architecture of AITL

AITLは以下の **三層構造（Layered Architecture）** によって構成されます：
```
┌──────────────┐
│ Logic Layer  │ ← 状態認識、因果推論、自己修復などの推論機能
├──────────────┤
│ Control Layer│ ← MPC / PID / ロバスト制御による信号生成
├──────────────┤
│ Physical Layer│ ← センサノイズ・動力学・外乱の物理モデリング
└──────────────┘
```
| 層 / Layer         | 説明 / Description |
|--------------------|--------------------|
| **Logic Layer**     | 状態認識、制約推論、目標生成、自己修復などの論理的推論を担当。論理プログラミングや因果推論も含む。<br>Responsible for logical inference, state recognition, constraint reasoning, goal generation, and self-repair logic. Includes logic programming and causal inference. |
| **Control Layer**   | 推論結果に基づき制御信号を生成。MPC（Model Predictive Control）、PID、ロバスト制御などを用いる。<br>Generates control signals based on logic outputs using MPC, PID, or robust control. |
| **Physical Layer**  | ロボットやドローン等の物理動力学、センサノイズ、外乱をモデル化。<br>Models physical dynamics, sensor noise, and external disturbances. |

---

## 理論と実装の関係性  
Relationship Between Theory and Implementation

- **AITL v1.0** は「設計図（Blueprint）」としての独立した理論体系です。  
- **AITL v2.0** では、この理論を内包したうえで実装や応用に展開されます。  

よって、理論と実装は断絶しておらず、**継続的・階層的に接続された構造**を持ちます。

---

## 応用例（v2.0の展望）  
Examples of v2.0 Implementations

以下は、v1.0の理論に基づく将来的な実装例の一部です：

| プロジェクト名（日本語） | Project Name (English) | 概要 / Description |
|--------------------------|-------------------------|---------------------|
| **AITL-R**               | AITL-R                  | ロボット向けの障害推論・冗長制御などを含む実装例。<br>Robotic implementation including fault inference and redundancy control. |
| **SkyEdge**              | SkyEdge                 | ドローン飛行制御と自己修復判断を実装。<br>Drone flight control and self-repair decision making. |
| **OpenSim-AITL**         | OpenSim-AITL            | 物理層モデリングと強化学習の統合シミュレーション。<br>Simulation integrating physical modeling and reinforcement learning. |

---

## 🔍 各層の詳細文書 / Subtheory Documents

AITL各層に関する理論的な詳細は以下の文書群で定義されています：

| 層 / Layer     | リンク / File                          | 内容 / Description |
|------------------|-----------------------------------------|--------------------|
| 推論層 / Logic    | [reasoning/mdp.md](./reasoning/mdp.md)         | MDPに基づく意思決定モデル、価値関数と報酬構造<br>MDP-based decision models, value functions, and reward structure. |
| 制御層 / Control  | [control/state_space.md](./control/state_space.md) | 状態空間表現、制御対象の抽象化と設計原理<br>State-space abstraction and control design principles. |
| 物理層 / Physics  | [physics/sensor_modeling.md](./physics/sensor_modeling.md) | センサノイズ、物理モデル、現実世界の外乱<br>Sensor noise modeling, physical systems, and disturbances. |
| 共通定義 / Common | [common/state_representation.md](./common/state_representation.md) | 各層に共通する状態ベクトル・変数記述<br>State variables and representations shared across layers. |
| 参考文献 / Refs   | [references/bibliography.md](./references/bibliography.md) | 関連理論、先行研究、背景資料<br>References and related theories. |

📌 全体構造は `index.md` に整理されています：  
👉 [理論インデックスへ](./index.md)

---

## Author

**Shinichi Samizo（三溝 真一）**  
Creator and lead theorist of the AITL framework.  
[GitHub Profile](https://github.com/Samizo-AITL)

---

## Contact

ご質問・提案は GitHub Issue またはメールにてご連絡ください。  
Feel free to reach out via [GitHub Issues](https://github.com/Samizo-AITL) or email.

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](../LICENSE) file for details.

---
