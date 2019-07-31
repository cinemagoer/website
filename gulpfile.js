var gulp = require('gulp');

gulp.task('sass', function () {
    const sass = require('gulp-sass');
    sass.compiler = require('node-sass');
    return gulp.src('./theme/sass/**/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('./assets/static/'));
});

gulp.task('uncss', function () {
    const postcss = require('gulp-postcss');
    const uncss = require('postcss-uncss');
    return gulp.src('./assets/static/imdbpy.css')
        .pipe(postcss([
            uncss({
                html: ['./_build/**/*.html']
            })
        ]))
        .pipe(gulp.dest('./theme/css/'));
});

gulp.task('cssmin', function () {
    const cssmin = require('gulp-cssmin');
    return gulp.src('./theme/css/imdbpy.css')
        .pipe(cssmin())
        .pipe(gulp.dest('./assets/static/'));
});

gulp.task('build', gulp.series('sass'));
gulp.task('after_build', gulp.series('uncss', 'cssmin'));
gulp.task('watch', function () {
    return gulp.watch('./theme/sass/**/*.scss', gulp.series('build', 'after_build'));
});

gulp.task('default', gulp.series('build'));
