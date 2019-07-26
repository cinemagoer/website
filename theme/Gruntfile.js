module.exports = function (grunt) {
    grunt.initConfig({
        uncss: {
            dist: {
                files: [
                    { src: '../_build/**/*.html', dest: '../assets/static/_imdbpy.css' }
                ]
            }
        },
        cssmin: {
            dist: {
                files: [
                    { src: '../assets/static/_imdbpy.css', dest: '../assets/static/imdbpy.css' }
                ]
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-uncss');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // Default tasks.
    grunt.registerTask('default', ['uncss', 'cssmin']);
};
