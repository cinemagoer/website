var gulp = require('gulp');

gulp.task('css', function () {
    const sass = require('gulp-sass');
    sass.compiler = require('node-sass');

    const postcss = require('gulp-postcss');
    const uncss = require('postcss-uncss');

    return gulp.src('./theme/sass/**/*.scss')
        .pipe(sass())
        .pipe(postcss([uncss({html: ['./_build/**/*.html']})]))
        .pipe(gulp.dest('./theme/css/'));
});

gulp.task('cssmin', function () {
    const cssmin = require('gulp-cssmin');

    return gulp.src('./theme/css/*.css')
        .pipe(cssmin())
        .pipe(gulp.dest('./assets/static/'));
});

gulp.task('build', gulp.series('css', 'cssmin'));
gulp.task('default', gulp.series('build'));
