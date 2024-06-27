# API Documentation / APIドキュメント

## Functions / 関数

### `load_data(file_path)`

- **English**: Loads the stock prices dataset from the specified file path.
- **日本語**: 指定されたファイルパスから株価データセットを読み込みます。

**Parameters / パラメータ**:
- `file_path` (str): Path to the CSV file containing stock prices / 株価を含むCSVファイルへのパス。

**Returns / 戻り値**:
- `pd.DataFrame`: Loaded data as a pandas DataFrame / pandas DataFrameとして読み込まれたデータ。

### `build_model(input_shape)`

- **English**: Builds and returns an LSTM model.
- **日本語**: LSTMモデルを構築して返します。

**Parameters / パラメータ**:
- `input_shape` (tuple): Shape of the input data / 入力データの形状。

**Returns / 戻り値**:
- `tf.keras.Model`: Compiled LSTM model / コンパイルされたLSTMモデル。

