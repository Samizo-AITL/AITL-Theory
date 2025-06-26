# AITL - All-in-Theory Logic 理論コア

---

## 概要（Overview）

AITL（All-in-Theory Logic）は、次世代AIシステムのための**完全理論ベースの階層アーキテクチャ**です。  
このリポジトリは、AITLの中核をなす**理論構造（v1.0）**をまとめています。  

---

## Versioning and Role of This Directory / バージョン体系と本ディレクトリの役割

AITLは一つの統一アーキテクチャであり、バージョンはその進化段階を示します。

| バージョン名 | 内容（日本語） | 内容（英語） |
|--------------|----------------|--------------|
| **AITL v1.0 (Theory only)** | 推論・制御・物理の三層理論モデルを抽象的に定義した理論コア。 | Abstract core theory defining the three-layer model: Logic, Control, Physical. |
| **AITL v2.0 (Theory + Implementation)** | v1.0の理論を基に具体的な実装・応用を加えた拡張版。 | Extended version adding concrete implementations and applications based on v1.0 theory. |

🧠 **本リポジトリは「AITL v1.0 (Theory only)」の理論部分を扱います。**  
v2.0は理論を含みつつ実装と応用を加えた段階であり、理論はすべての応用の基盤です。

---

## AITLの三層構造 / Three-layer Architecture of AITL

AITLは以下の3層構造で構成されています：

| 層（日本語） | Layer (English) | 説明 / Description |
|-------------|-----------------|--------------------|
| 推論層       | Logic Layer     | 状態認識、制約推論、目標生成、自己修復などの論理的推論を担当。論理プログラミングや因果推論も含む。<br>Responsible for logical inference, state recognition, constraint reasoning, goal generation, and self-repair logic. Includes logic programming and causal inference. |
| 制御層       | Control Layer   | 推論層の出力を基に制御信号を生成。モデル予測制御（MPC）、PID制御、ロバスト制御などを用いる。<br>Generates control signals based on logic layer output, employing MPC, PID, and robust control methods. |
| 物理層       | Physical Layer  | ロボットやドローンの物理動力学、センサノイズ、外乱をモデル化。<br>Models physical dynamics, sensor noise, and disturbances of real-world systems. |

---

## 理論と実装の関係性 / Relationship Between Theory and Implementation

- AITLの理論（v1.0）は独立した設計図であり、  
- これを基にした応用・実装がv2.0として発展しています。  

そのため、理論と実装は「分裂」ではなく、  
**理論を含む「進化のステージ」として連続した関係**です。

---

## 応用例（v2.0のイメージ） / Examples of v2.0 Implementations

| プロジェクト名 (日本語) | Project Name (English) | 概要 / Description |
|-----------------|--------------------|--------------------|
| AITL-R          | AITL-R             | ロボット向けの障害推論・冗長制御などを含む実装例。<br>Robotic implementation including fault inference and redundancy control. |
| SkyEdge         | SkyEdge            | ドローン飛行制御と自己修復判断を実装。<br>Drone flight control and self-repair decision making. |
| OpenSim-AITL    | OpenSim-AITL       | 物理層モデリングと強化学習の統合シミュレーション。<br>Simulation integrating physical modeling and reinforcement learning. |

---

## ライセンス・著者 / License & Author

- ライセンス：MIT License（オープンソース）  
- 理論開発責任者：三溝 真一（Shinichi Samizo）  

---

## 連絡先 / Contact

ご質問やフィードバックはIssueやメールでお気軽にどうぞ。
