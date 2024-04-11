# pdf2txt

pdf2txt is a straightforward Python script that extracts text from PDF files, cleans it by removing hyphenated line breaks and reducing multiple whitespace characters to single spaces, and saves the result to a text file. It leverages the `pdfminer.six` library to perform the extraction efficiently.

## Installation

To use pdf2txt, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/daishir0/pdf2txt.git
cd pdf2txt
```

1. Navigate into the cloned repository:

```bash
cd pdf2txt
```

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

# Usage

To convert a PDF file to text, run:

```
python pdf2txt.py target.pdf
```

Replace target.pdf with the path to your PDF file. The script will create a .txt file with the same name as the PDF in the same directory.

# Notes

- This script is intended for simple text extraction and may not handle complex PDF layouts or images.
- Ensure the PDF file is text-based and not a scanned image document for optimal results.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

---

# pdf2txt

pdf2txtは、PDFファイルからテキストを抽出し、ハイフンによる改行を削除して不要なスペースを一つに減らし、結果をテキストファイルに保存するシンプルなPythonスクリプトです。テキスト抽出にはpdfminer.sixライブラリを効率的に使用しています。

# インストール方法

pdf2txtを使用するには、レポジトリをクローンして、ディレクトリ変更後にrequirements.txtでライブラリをインストールしてください。

```bash
git clone https://github.com/daishir0/pdf2txt.git
cd pdf2txt
pip install -r requirements.txt
```

# 使い方

PDFファイルをテキストに変換するには、以下を実行します：

```bash
python pdf2txt.py target.pdf
```

target.pdfをPDFファイルのパスに置き換えてください。スクリプトはPDFと同じ名前の.txtファイルを同じディレクトリに作成します。

# 注意点

- このスクリプトはシンプルなテキスト抽出を目的としており、複雑なPDFレイアウトや画像は処理しません。
- PDFファイルがテキストベースであり、スキャンされた画像ドキュメントでないことを確認してください。

# ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細はLICENSEファイルを参照してください。


