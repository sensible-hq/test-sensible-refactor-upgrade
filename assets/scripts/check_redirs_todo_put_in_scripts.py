# check redirects from mintlify migration

import requests

def check_redirects(urls):
    results = []
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=True, timeout=5)
            results.append((url, response.url, response.status_code))
        except requests.exceptions.RequestException as e:
            results.append((url, None, str(e)))
    return results

# list of URLs
urls = [
    # check redirects from mintlify migration

import requests

base_path = "https://sensible.mintlify.app"

#base_path = "https://docs.sensible.so/"

def check_redirects(urls):
    results = []
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=True, timeout=5)
            results.append((url, response.url, response.status_code))
        except requests.exceptions.RequestException as e:
            results.append((url, None, str(e)))
    return results

# list of URLs
urls = [
    base_path + "/docs/accuracy-measures",
    base_path + "/docs/add-computed-fields",
    base_path + "/docs/anchor",
    base_path + "/docs/anchor-nuances",
    base_path + "/docs/api-reference",
    base_path + "/docs/api-tutorial-async-1",
    base_path + "/docs/api-tutorial-async-2",
    base_path + "/docs/api-tutorial-sync",
    base_path + "/docs/api-tutorial-webhook",
    base_path + "/docs/author",
    base_path + "/docs/bag-of-words",
    base_path + "/docs/batch-api",
    base_path + "/docs/box",
    base_path + "/docs/checkbox",
    base_path + "/docs/classify",
    base_path + "/docs/color",
    base_path + "/docs/column",
    base_path + "/docs/concatenate",
    base_path + "/docs/confidence",
    base_path + "/docs/constant",
    base_path + "/docs/copy-from-sections",
    base_path + "/docs/copy-to-section",
    base_path + "/docs/coverage",
    base_path + "/docs/custom-computation",
    base_path + "/docs/deprecated-bag-of-words",
    base_path + "/docs/deprecated-invoice",
    base_path + "/docs/deprecated-key-value",
    base_path + "/docs/deprecated-page-filter",
    base_path + "/docs/deprecated-query",
    base_path + "/docs/deprecated-table",
    base_path + "/docs/deprecated-tfidf",
    base_path + "/docs/deprecated-topic",
    base_path + "/docs/deskew",
    base_path + "/docs/document-range",
    base_path + "/docs/email",
    base_path + "/docs/examples",
    base_path + "/docs/excel-reference",
    base_path + "/docs/fallbacks",
    base_path + "/docs/field-order",
    base_path + "/docs/file-types",
    base_path + "/docs/fingerprint",
    base_path + "/docs/fingerprint-mode",
    base_path + "/docs/fixed-table",
    base_path + "/docs/get-file-metadata",
    base_path + "/docs/getting-started",
    base_path + "/docs/getting-started-ai",
    base_path + "/docs/go-live",
    base_path + "/docs/handwriting",
    base_path + "/docs/integrate",
    base_path + "/docs/intersection",
    base_path + "/docs/label",
    base_path + "/docs/library-quickstart",
    base_path + "/docs/ligature",
    base_path + "/docs/ligatures",
    base_path + "/docs/lines",
    base_path + "/docs/list",
    base_path + "/docs/list-tips",
    base_path + "/docs/mapper",
    base_path + "/docs/match",
    base_path + "/docs/match-arrays",
    base_path + "/docs/merge-lines",
    base_path + "/docs/method",
    base_path + "/docs/metrics",
    base_path + "/docs/nearest-checkbox",
    base_path + "/docs/nlp",
    base_path + "/docs/nlp-table",
    base_path + "/docs/ocr",
    base_path + "/docs/ocr-engine",
    base_path + "/docs/ocr-level",
    base_path + "/docs/ocr-preprocessor",
    base_path + "/docs/page-range",
    base_path + "/docs/paragraph",
    base_path + "/docs/passthrough",
    base_path + "/docs/performance",
    base_path + "/docs/pick-values",
    base_path + "/docs/portfolio",
    base_path + "/docs/prompt",
    base_path + "/docs/query-group",
    base_path + "/docs/query-group-tips",
    base_path + "/docs/quickstart",
    base_path + "/docs/regex",
    base_path + "/docs/region",
    base_path + "/docs/remove-footer",
    base_path + "/docs/remove-header",
    base_path + "/docs/remove-page",
    base_path + "/docs/repeat-layouts",
    base_path + "/docs/rotate-page",
    base_path + "/docs/row",
    base_path + "/docs/scale",
    base_path + "/docs/sdk-guides",
    base_path + "/docs/section-nuances",
    base_path + "/docs/sections-example-copy-from-sections",
    base_path + "/docs/sections-example-copy-to-section",
    base_path + "/docs/sections-example-external-range",
    base_path + "/docs/sections-example-labeled-rows",
    base_path + "/docs/sections-example-loss-run",
    base_path + "/docs/sections-example-nested-columns",
    base_path + "/docs/sections-example-nested-table",
    base_path + "/docs/sections-example-table-grid",
    base_path + "/docs/sections-example-zip",
    base_path + "/docs/senseml",
    base_path + "/docs/senseml-reference-introduction",
    base_path + "/docs/signature",
    base_path + "/docs/split",
    base_path + "/docs/split-lines",
    base_path + "/docs/summarizer",
    base_path + "/docs/suppress-output",
    base_path + "/docs/table-methods",
    base_path + "/docs/table-tips",
    base_path + "/docs/test-before-integrating-configs",
    base_path + "/docs/text-table",
    base_path + "/docs/troubleshoot",
    base_path + "/docs/troubleshoot-llms",
    base_path + "/docs/types",
    base_path + "/docs/ui",
    base_path + "/docs/validate-extractions",
    base_path + "/docs/verbosity",
    base_path + "/docs/zapier-getting-started",
    base_path + "/docs/zapier-tutorial-2",
    base_path + "/docs/zip",
    base_path + "/reference/authentication",
    base_path + "/reference/classify-document",
    base_path + "/reference/classify-document-sync",
    base_path + "/reference/create-configuration",
    base_path + "/reference/create-document-type",
    base_path + "/reference/create-reference-document",
    base_path + "/reference/delete-configuration",
    base_path + "/reference/delete-configuration-by-version",
    base_path + "/reference/delete-document-type",
    base_path + "/reference/delete-reference-document",
    base_path + "/reference/delete-reference-document-association",
    base_path + "/reference/extract-all-text-from-reference-document",
    base_path + "/reference/extract-data-from-a-document",
    base_path + "/reference/extract-data-from-a-document-with-config",
    base_path + "/reference/extract-from-url",
    base_path + "/reference/extract-from-url-portfolio",
    base_path + "/reference/extract-from-url-using-config",
    base_path + "/reference/generate-upload-url",
    base_path + "/reference/generate-upload-url-portfolio",
    base_path + "/reference/generate-upload-url-using-specified-config",
    base_path + "/reference/get-configuration",
    base_path + "/reference/get-configuration-by-version",
    base_path + "/reference/get-configuration-versions",
    base_path + "/reference/get-csv-extraction",
    base_path + "/reference/get-document-type",
    base_path + "/reference/get-excel-extraction",
    base_path + "/reference/get-reference-document",
    base_path + "/reference/introduction",
    base_path + "/reference/list-configurations",
    base_path + "/reference/list-document-types",
    base_path + "/reference/list-extractions",
    base_path + "/reference/list-reference-documents",
    base_path + "/reference/publish-configuration-by-version",
    base_path + "/reference/retrieving-results",
    base_path + "/reference/statistics",
    base_path + "/reference/update-configuration",
    base_path + "/reference/update-document-type",
    base_path + "/reference/update-reference-document",
    base_path + "/docs/index-methods"
    base_path + "/docs/index-llm-based-methods"
    base_path + "/docs/index-field-query-object"
    base_path + "/docs/index-document-type-settings"
    base_path + "/docs/index-config-settings"
    base_path + "/docs/index-concepts"
    base_path + "/docs/index-computed-field-methods"
    base_path + "/docs/index-advanced-computed-field-methods"
    base_path + "/docs/index-prompt-tips"
    base_path + "/docs/index-app-guide"
    base_path + "/docs/index-zapier"
    base_path + "/docs/index-quick-extraction"
    base_path + "/docs/index-tutorials"
    base_path + "/docs/index-api-tutorial"
    base_path + "/docs/index-sections"
    base_path + "/docs/index-preprocessors"


]

# Check redirects for the list of URLs
results = check_redirects(urls)

# Write the results to a text file
with open("redirect_results.txt", "w+") as file:
    for result in results:
        file.write(f"{result}\n")

print("Results have been written to redirect_results.txt")













]

# Check redirects for the list of URLs
results = check_redirects(urls)

# Write the results to a text file
with open("redirect_results.txt", "w+") as file:
    for result in results:
        file.write(f"{result}\n")

print("Results have been written to redirect_results.txt")
