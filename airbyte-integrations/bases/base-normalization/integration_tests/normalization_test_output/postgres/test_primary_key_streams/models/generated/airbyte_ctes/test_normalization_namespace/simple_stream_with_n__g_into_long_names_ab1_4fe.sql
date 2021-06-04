{{ config(alias="simple_stream_with_n__g_into_long_names_ab1", schema="_airbyte_test_normalization_namespace", tags=["top-level-intermediate"]) }}
-- SQL model to parse JSON blob stored in a single column and extract into separated field columns as described by the JSON Schema
select
    {{ json_extract_scalar('_airbyte_data', ['id']) }} as {{ adapter.quote('id') }},
    {{ json_extract_scalar('_airbyte_data', ['date']) }} as {{ adapter.quote('date') }},
    _airbyte_emitted_at
from {{ source('test_normalization_namespace', '_airbyte_raw_simple_stream_with_namespace_resulting_into_long_names') }}
-- simple_stream_with_n__lting_into_long_names
