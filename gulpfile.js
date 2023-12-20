const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();

function css() {
    return gulp.src('frontend/sass/style.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('out'))
        .pipe(browserSync.stream())
}

function watch() {
    browserSync.init({
        server: {
            baseDir: './'
        }
    });
    gulp.watch('frontend/sass', css);
    gulp.watch('index.html').on('change', browserSync.reload);
    gulp.watch('app/flask_app/templates').on('change', browserSync.reload);
    gulp.watch('frontend/js').on('change', browserSync.reload);
}

function defaultTask(cb) {
    console.log('hello gulp world');
    cb();
}

exports.default = defaultTask
exports.style = css;
exports.watch = watch;
