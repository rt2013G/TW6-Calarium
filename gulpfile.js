const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const browserSync = require('browser-sync').create();

function css() {
    return gulp.src('app/sass/style.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('app/out'))
        .pipe(browserSync.stream())
}

function watch() {
    browserSync.init({
        server: {
            baseDir: './'
        }
    });
    gulp.watch('app/sass', css);
    gulp.watch('index.html').on('change', browserSync.reload);
}

function defaultTask(cb) {
    console.log('hello gulp world');
    cb();
}

exports.default = defaultTask
exports.style = css;
exports.watch = watch;
