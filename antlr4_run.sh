#!/bin/bash

echo "Running ANTLR script..."

ANTLR_JAR_PATH=antlr-4.13.1-complete.jar

PROJECT_ROOT=$(pwd)

GRAMMAR_DIR=$PROJECT_ROOT/src/grammar_files

OUTPUT_DIR=$GRAMMAR_DIR/generated

if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir "$OUTPUT_DIR"
fi

echo "Enter grammar file name with extension: "
read GrammarFile

echo "Generating ANTLR files for ${GrammarFile}"
java -jar "$ANTLR_JAR_PATH" -Dlanguage=Python3 -o "$OUTPUT_DIR" "$GRAMMAR_DIR/$GrammarFile" -visitor -no-listener
echo "Generation complete, thanks for using linux"

