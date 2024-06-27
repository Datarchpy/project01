# Design Document / 設計ドキュメント

## System Architecture / システムアーキテクチャ

- **English**: The system consists of the following components:
- **日本語**: システムは以下のコンポーネントで構成されています。

  - **Data Loader / データローダー**: Loads and preprocesses the stock prices dataset / 株価データセットを読み込み、前処理します。
  - **LSTM Model / LSTMモデル**: Builds and trains the LSTM model / LSTMモデルを構築し、トレーニングします。
  - **Evaluation / 評価**: Evaluates the model performance and visualizes results / モデルの性能を評価し、結果を可視化します。

## Data Flow / データフロー

1. **English**: Data Loading: `data/stock_prices.csv`
   **日本語**: データの読み込み: `data/stock_prices.csv`
2. **English**: Data Preprocessing: Normalization and sequence generation
   **日本語**: データ前処理: 正規化とシーケンス生成
3. **English**: Model Training: LSTM model with specified hyperparameters
   **日本語**: モデルトレーニング: 指定されたハイパーパラメータでのLSTMモデル
4. **English**: Evaluation: Calculation of RMSE and plotting predicted vs actual prices
   **日本語**: 評価: RMSEの計算と予測価格と実際の価格のプロット

## Module Design / モジュール設計

- **English**:
  - `src/data_loader.py`: Contains functions for loading and preprocessing data / データの読み込みと前処理を行う関数が含まれています。
  - `src/model.py`: Contains the LSTM model definition and training code / LSTMモデルの定義とトレーニングコードが含まれています。
  - `src/evaluation.py`: Contains functions for ev

