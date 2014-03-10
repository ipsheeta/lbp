# Settings for django pipeline
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

#PIPELINE_LESS_BINARY = '/usr/bin/lessc'
#PIPELINE_TEMPLATE_EXT = ".mustache"
#PIPELINE_TEMPLATE_FUNC = "Mustache.template"

PIPELINE_CSS = {
    'bootstrap': {
        'source_filenames': (
            'bootstrap/css/bootstrap.css',
        ),
        'output_filename': 'css/bootstrap.css',
    },
    'home_page': {
        'source_filenames': (
            'less/home.less',
            'less/nav.less',
        ),
        'output_filename': 'css/home.css',
    },
    'internal_page': {
        'source_filenames': (
            'less/home.less',
            'less/internal.less',
            'less/nav.less',
            'less/ys-color1.less',
        ),
        'output_filename': 'css/internal.css',
    },

}

PIPELINE_JS = {
    'common': {
        'source_filenames': (),
        'output_filename': ''
    }
}