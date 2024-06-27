;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         A.N.Other <myemail@nowhere.com>
;
; Script Function:
;	autoexpand snippets for redirects

; Define hotstrings that triggers when a keyword is typed followed by the Tab key



::/prompt::
SendInput /llm-based-extractions/prompt
return

::/author::
SendInput /welcome/author
return

::/integrate::
SendInput /welcome/integrate
return

::/sections-example-zip::
SendInput /senseml-reference/sections/sections-example-zip
return

::/getting-started-ai::
SendInput /welcome/getting-started-ai
return

::/sections-example-table-grid::
SendInput /senseml-reference/sections/sections-example-table-grid
return

::/sections-example-nested-table::
SendInput /senseml-reference/sections/sections-example-nested-table
return

::/sections-example-nested-columns::
SendInput /senseml-reference/sections/sections-example-nested-columns
return

::/sections-example-loss-run::
SendInput /senseml-reference/sections/sections-example-loss-run
return

::/sections-example-labeled-rows::
SendInput /senseml-reference/sections/sections-example-labeled-rows
return

::/sections-example-external-range::
SendInput /senseml-reference/sections/sections-example-external-range
return

::/sections-example-copy-to-section::
SendInput /senseml-reference/sections/sections-example-copy-to-section
return

::/sections-example-copy-from-sections::
SendInput /senseml-reference/sections/sections-example-copy-from-sections
return

::/split-lines::
SendInput /senseml-reference/preprocessors/split-lines
return

::/scale::
SendInput /senseml-reference/preprocessors/scale
return

::/rotate-page::
SendInput /senseml-reference/preprocessors/rotate-page
return

::/remove-header::
SendInput /senseml-reference/preprocessors/remove-header
return

::/remove-footer::
SendInput /senseml-reference/preprocessors/remove-footer
return

::/page-range::
SendInput /senseml-reference/preprocessors/page-range
return

::/ocr-preprocessor::
SendInput /senseml-reference/preprocessors/ocr-preprocessor
return

::/nlp::
SendInput /senseml-reference/preprocessors/nlp
return

::/merge-lines::
SendInput /senseml-reference/preprocessors/merge-lines
return

::/ligature::
SendInput /senseml-reference/preprocessors/ligature
return

::/deskew::
SendInput /senseml-reference/preprocessors/deskew
return

::/text-table::
SendInput /senseml-reference/methods/text-table
return

::/signature::
SendInput /senseml-reference/methods/signature
return

::/row::
SendInput /senseml-reference/methods/row
return

::/region::
SendInput /senseml-reference/methods/region
return

::/regex::
SendInput /senseml-reference/methods/regex
return

::/passthrough::
SendInput /senseml-reference/methods/passthrough
return

::/paragraph::
SendInput /senseml-reference/methods/paragraph
return

::/nearest-checkbox::
SendInput /senseml-reference/methods/nearest-checkbox
return

::/label::
SendInput /senseml-reference/methods/label
return

::/intersection::
SendInput /senseml-reference/methods/intersection
return

::/fixed-table::
SendInput /senseml-reference/methods/fixed-table
return

::/document-range::
SendInput /senseml-reference/methods/document-range
return

::/column::
SendInput /senseml-reference/methods/column
return

::/checkbox::
SendInput /senseml-reference/methods/checkbox
return

::/box::
SendInput /senseml-reference/methods/box
return

::/summarizer::
SendInput /senseml-reference/llm-based-methods/summarizer
return

::/query-group::
SendInput /senseml-reference/llm-based-methods/query-group
return

::/nlp-table::
SendInput /senseml-reference/llm-based-methods/nlp-table
return

::/list::
SendInput /senseml-reference/llm-based-methods/list
return

::/types::
SendInput /senseml-reference/field-query-object/types
return

::/method::
SendInput /senseml-reference/field-query-object/method
return

::/match::
SendInput /senseml-reference/field-query-object/match
return

::/anchor::
SendInput /senseml-reference/field-query-object/anchor
return

::/ocr-level::
SendInput /senseml-reference/document-type-settings/ocr-level
return

::/ocr-engine::
SendInput /senseml-reference/document-type-settings/ocr-engine
return

::/fingerprint-mode::
SendInput /senseml-reference/document-type-settings/fingerprint-mode
return

::/verbosity::
SendInput /senseml-reference/config-settings/verbosity
return

::/fingerprint::
SendInput /senseml-reference/config-settings/fingerprint
return

::/table-methods::
SendInput /senseml-reference/concepts/table-methods
return

::/senseml::
SendInput /senseml-reference/concepts/senseml
return

::/section-nuances::
SendInput /senseml-reference/concepts/section-nuances
return

::/ocr::
SendInput /senseml-reference/concepts/ocr
return

::/match-arrays::
SendInput /senseml-reference/concepts/match-arrays
return

::/lines::
SendInput /senseml-reference/concepts/lines
return

::/ligatures::
SendInput /senseml-reference/concepts/ligatures
return

::/file-types::
SendInput /senseml-reference/concepts/file-types
return

::/field-order::
SendInput /senseml-reference/concepts/field-order
return

::/coverage::
SendInput /senseml-reference/concepts/coverage
return

::/bag-of-words::
SendInput /senseml-reference/concepts/bag-of-words
return

::/anchor-nuances::
SendInput /senseml-reference/concepts/anchor-nuances
return

::/accuracy-measures::
SendInput /senseml-reference/concepts/accuracy-measures
return

::/zip::
SendInput /senseml-reference/computed-field-methods/zip
return

::/suppress-output::
SendInput /senseml-reference/computed-field-methods/suppress-output
return

::/split::
SendInput /senseml-reference/computed-field-methods/split
return

::/pick-values::
SendInput /senseml-reference/computed-field-methods/pick-values
return

::/mapper::
SendInput /senseml-reference/computed-field-methods/mapper
return

::/constant::
SendInput /senseml-reference/computed-field-methods/constant
return

::/concatenate::
SendInput /senseml-reference/computed-field-methods/concatenate
return

::/get-file-metadata::
SendInput /senseml-reference/advanced-computed-field-methods/get-file-metadata
return

::/custom-computation::
SendInput /senseml-reference/advanced-computed-field-methods/custom-computation
return

::/copy-to-section::
SendInput /senseml-reference/advanced-computed-field-methods/copy-to-section
return

::/copy-from-sections::
SendInput /senseml-reference/advanced-computed-field-methods/copy-from-sections
return

::/add-computed-fields::
SendInput /senseml-reference/advanced-computed-field-methods/add-computed-fields
return

::/senseml-reference-introduction::
SendInput /senseml-reference/senseml-reference-introduction
return

::/table-tips::
SendInput /llm-based-extractions/prompt-tips/table-tips
return

::/query-group-tips::
SendInput /llm-based-extractions/prompt-tips/query-group-tips
return

::/list-tips::
SendInput /llm-based-extractions/prompt-tips/list-tips
return

::/ui::
SendInput /layout-based-extractions/app-guide/ui
return

::/color::
SendInput /layout-based-extractions/app-guide/color
return

::/repeat-layouts::
SendInput /layout-based-extractions/repeat-layouts
return

::/portfolio::
SendInput /layout-based-extractions/portfolio
return

::/library-quickstart::
SendInput /layout-based-extractions/library-quickstart
return

::/getting-started::
SendInput /layout-based-extractions/getting-started
return

::/zapier-tutorial-2::
SendInput /integrations/zapier/zapier-tutorial-2
return

::/zapier-getting-started::
SendInput /integrations/zapier/zapier-getting-started
return

::/excel-reference::
SendInput /integrations/quick-extraction/excel-reference
return

::/sdk-guides::
SendInput /integrations/sdk-guides


::/quickstart::
SendInput /integrations/quickstart
return

::/classify::
SendInput /document-type-classification/classify
return

::/troubleshoot::
SendInput /best-practices/tutorials/troubleshoot
return

::/test-before-integrating-configs::
SendInput /best-practices/tutorials/test-before-integrating-configs
return

::/performance::
SendInput /best-practices/tutorials/performance
return

::/handwriting::
SendInput /best-practices/tutorials/handwriting
return

::/go-live::
SendInput /best-practices/tutorials/go-live
return

::/fallbacks::
SendInput /best-practices/tutorials/fallbacks
return

::/validate-extractions::
SendInput /best-practices/validate-extractions
return

::/troubleshoot-llms::
SendInput /best-practices/troubleshoot-llms
return

::/metrics::
SendInput /best-practices/metrics
return

::/confidence::
SendInput /best-practices/confidence
return

::/api-tutorial-webhook::
SendInput /api-guides/api-tutorial/api-tutorial-webhook
return

::/api-tutorial-sync::
SendInput /api-guides/api-tutorial/api-tutorial-sync
return

::/api-tutorial-async-2::
SendInput /api-guides/api-tutorial/api-tutorial-async-2
return

::/api-tutorial-async-1::
SendInput /api-guides/api-tutorial/api-tutorial-async-1
return

::/examples::
SendInput /api-guides/examples
return

::/deprecated-table::
SendInput /senseml-reference/deprecated-features/deprecated-table
return

::/deprecated-topic::
SendInput /senseml-reference/deprecated-features/deprecated-topic
return

::/deprecated-tfidf::
SendInput /senseml-reference/deprecated-features/deprecated-tfidf
return

::/deprecated-query::
SendInput /senseml-reference/deprecated-features/deprecated-query
return

::/deprecated-invoice::
SendInput /senseml-reference/deprecated-features/deprecated-invoice
return

::/deprecated-page-filter::
SendInput /senseml-reference/deprecated-features/deprecated-page-filter
return

::/deprecated-key-value::
SendInput /senseml-reference/deprecated-features/deprecated-key-value
return

::/deprecated-bag-of-words::
SendInput /senseml-reference/deprecated-features/deprecated-bag-of-words
return

::/api-reference::
SendInput /api-guides/api-reference
return

::/classify-document-by-type::
SendInput /api-reference/classification/document/classify-document-by-type
return

::/classify-document-sync::
SendInput /api-reference/classification/document/classify-document-sync
return

::/introduction::
SendInput /api-reference/introduction
return

::/authentication::
SendInput /api-reference/authentication
return

::/retrieve-extraction-by-id::
SendInput /api-reference/extraction/retrieve-extractions/retrieve-extraction-by-id
return

::/list-extractions::
SendInput /api-reference/extraction/retrieve-extractions/list-extractions
return

::/get-extraction-statistics::
SendInput /api-reference/extraction/retrieve-extractions/get-extraction-statistics
return

::/extract-portfolio-at-your-url::
SendInput /api-reference/extraction/portfolio/extract-portfolio-at-your-url
return

::/extract-portfolio-at-a-sensible-url::
SendInput /api-reference/extraction/portfolio/extract-portfolio-at-a-sensible-url
return

::/get-excel-extraction::
SendInput /api-reference/extraction/get-excel-from-documents/get-excel-extraction
return

::/get-csv-extraction::
SendInput /api-reference/extraction/get-excel-from-documents/get-csv-extraction
return

::/extract-doc-at-your-url::
SendInput /api-reference/extraction/document/extract-doc-at-your-url
return



::/extract-doc-at-a-sensible-url::
SendInput /api-reference/extraction/document/extract-doc-at-a-sensible-url
return




::/extract-data-from-a-document::
SendInput /api-reference/extraction/document/extract-data-from-a-document
return



::/get-reference-document-metadata::
SendInput /api-reference/configuration/reference-document/get-reference-document-metadata
return



::/delete-reference-document::
SendInput /api-reference/configuration/reference-document/delete-reference-document
return

::/create-reference-document::
SendInput /api-reference/configuration/reference-document/create-reference-document
return

::/update-document-type::
SendInput /api-reference/configuration/document-type/update-document-type
return


::/get-document-type-metadata::
SendInput /api-reference/configuration/document-type/get-document-type-metadata
return

::/delete-document-type::
SendInput /api-reference/configuration/document-type/delete-document-type
return

::/create-document-type::
SendInput /api-reference/configuration/document-type/create-document-type
return

::/update-configuration::
SendInput /api-reference/configuration/configuration/update-configuration
return

::/publish-configuration-to-an-environment::
SendInput /api-reference/configuration/configuration/publish-configuration-to-an-environment
return

::/list-versions-for-a-configuration::
SendInput /api-reference/configuration/configuration/list-versions-for-a-configuration
return

::/list-configurations-in-a-document-type::
SendInput /api-reference/configuration/configuration/list-configurations-in-a-document-type
return

::/get-configuration::
SendInput /api-reference/configuration/configuration/get-configuration
return

::/get-configuration-by-version::
SendInput /api-reference/configuration/configuration/get-configuration-by-version
return

::/delete-draft-or-unpublish-configuration::
SendInput /api-reference/configuration/configuration/delete-draft-or-unpublish-configuration
return

::/delete-configuration::
SendInput /api-reference/configuration/configuration/delete-configuration
return

::/create-configuration-in-a-document-type::
SendInput /api-reference/configuration/configuration/create-configuration-in-a-document-type
return

::/methods::
SendInput /senseml-reference/methods/index-methods
return

::/llm-based-methods::
SendInput /senseml-reference/llm-based-methods/index-llm-based-methods
return

::/field-query-object::
SendInput /senseml-reference/field-query-object/index-field-query-object
return

::/document-type-settings::
SendInput /senseml-reference/document-type-settings/index-document-type-settings
return

::/config-settings::
SendInput /senseml-reference/config-settings/index-config-settings
return

::/concepts::
SendInput /senseml-reference/concepts/index-concepts
return

::/computed-field-methods::
SendInput /senseml-reference/computed-field-methods/index-computed-field-methods
return

::/advanced-computed-field-methods::
SendInput /senseml-reference/advanced-computed-field-methods/index-advanced-computed-field-methods
return

::/prompt-tips::
SendInput /llm-based-extractions/prompt-tips/index-prompt-tips
return

::/app-guide::
SendInput /layout-based-extractions/app-guide/index-app-guide
return

::/zapier::
SendInput /integrations/zapier/index-zapier
return

::/quick-extraction::
SendInput /integrations/quick-extraction/index-quick-extraction
return

::/tutorials::
SendInput /best-practices/tutorials/index-tutorials
return

::/api-tutorial::
SendInput /api-guides/api-tutorial/index-api-tutorial
return

::/sections::
SendInput /senseml-reference/sections/index-sections
return

::/preprocessors::
SendInput /senseml-reference/preprocessors/index-preprocessors
return

