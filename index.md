# AITL v1.0 理論インデックス / AITL v1.0 Theory Index

本ドキュメントは、AITL v1.0（理論）の全体構造を示すインデックスです。  
各層の詳細、共通定義、参考文献など、各資料へのリンクをご確認ください。

---

## 目次 / Table of Contents

1. [概要 / Overview](#概要--overview)
2. [三層アーキテクチャ / Three-layer Architecture](#三層アーキテクチャ--three-layer-architecture)
3. [各層の詳細ドキュメント / Detailed Documents by Layer](#各層の詳細ドキュメント--detailed-documents-by-layer)
    - [推論層 / Logic](#推論層--logic)
    - [制御層 / Control](#制御層--control)
    - [物理層 / Physics](#物理層--physics)
    - [共通定義 / Common](#共通定義--common)
4. [参考文献 / References](#参考文献--references)
5. [補助資料およびその他 / Additional Resources](#補助資料およびその他--additional-resources)

---

## 概要 / Overview

AITL（All-in-Theory Logic）は、次世代AIシステムのための完全理論ベースの階層アーキテクチャです。  
このリポジトリは、**AITL v1.0** の理論部分を扱い、推論、制御、物理の各層に関する詳細資料が整理されています。

---

## 三層アーキテクチャ / Three-layer Architecture

AITLは以下の三層から構成されています：

```
┌──────────────┐
│ Logic Layer  │  ← 推論機能（状態認識、因果推論、自己修復など）
├──────────────┤
│ Control Layer│  ← 制御機能（MPC、PID、ロバスト制御による信号生成）
├──────────────┤
│ Physical Layer│ ← 物理モデリング（センサノイズ、動力学、外乱）
└──────────────┘
```

各層の詳細は、以下の項目をご参照ください。

---

## 各層の詳細ドキュメント / Detailed Documents by Layer

### 推論層 / Logic  
- **資料**: [reasoning/mdp.md](./reasoning/mdp.md)  
- **内容**: マルコフ決定過程（MDP）に基づく意思決定モデル、価値関数、報酬設計など、推論層の基本理論を解説しています。

### 制御層 / Control  
- **資料**: [control/state_space.md](./control/state_space.md)  
- **内容**: 状態空間表現や、制御対象となるシステムの抽象化、MPC/PIDなどの制御原理に関する理論資料です。

### 物理層 / Physics  
- **資料**: [physics/sensor_modeling.md](./physics/sensor_modeling.md)  
- **内容**: センサノイズ、動力学、実世界の外乱に対する物理的モデリングの方法論を記述しています。

### 共通定義 / Common  
- **資料**: [common/state_representation.md](./common/state_representation.md)  
- **内容**: 各層で利用される共通の状態表現、変数の定義やフォーマットについてまとめています。

---

## 参考文献 / References

- **資料**: [references/bibliography.md](./references/bibliography.md)  
- **内容**: AITLに関連する先行研究や背景となる理論資料の一覧です。

---

## 補助資料およびその他 / Additional Resources

- **全体概要・構造図**  
  詳細な全体像は [theory/README.md](./README.md) に記述されています。  
- **GitHub Actionsなどの補助ファイル**  
  `.github/workflows` 以下のCI設定ファイルや、スクリプト（inject_mathjax.py.bak）も管理されていますが、理論本体の参照には含めていません。

---

本インデックスを活用し、各層および補助資料間の関係性や理論の全体像をご確認ください。
