module.exports = {
    outputDir: "vue-dist",
    assetsDir: "static/vue-static",
    devServer: {
        proxy: {
            "/api/*": {
                // Forwards all requests from vue dev server to django dev server
                target: "http://django:8000/",
            },
        },
    },
};
