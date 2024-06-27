#!/bin/bash

# Install dependencies (eslint and eslint-plugin-mdx) globally in a temporary directory
TEMP_DIR=$(mktemp -d)
npm install -g eslint eslint-plugin-mdx --prefix $TEMP_DIR

# Create an ESLint configuration file
cat <<EOL > .eslintrc.json
{
  "extends": [
    "plugin:mdx/recommended"
  ],
  "overrides": [
    {
      "files": ["*.mdx"],
      "extends": ["plugin:mdx/recommended"]
    }
  ]
}
EOL

# Run ESLint on all MDX files and output the result in JSON format
$TEMP_DIR/node_modules/.bin/eslint '**/*.mdx' --format json -o eslint-report.json

# Check if the report is not empty (indicating there are lint errors)
if [ -s eslint-report.json ]; then
  cat eslint-report.json
  exit 1
fi
