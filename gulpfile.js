const gulp = require("gulp");
const {series} = require('gulp');
const plugins = require('gulp-load-plugins')();
const chalk = require('chalk');

const inputFiles = './project/static/';
const outputFiles = './project/static/assets/';


gulp.task('minifyJS', function () {
    return gulp.src(inputFiles + 'js/*.js')
        .pipe(plugins.uglify())
        .pipe(plugins.concat('app.min.js'))
        .pipe(gulp.dest(outputFiles + 'js/'));
});

gulp.task('minifyCSS', function () {
    return gulp.src(inputFiles + 'css/*.css')
        .pipe(plugins.less())
        .pipe(plugins.autoprefixer())
        .pipe(plugins.concat('app.min.css'))
        .pipe(gulp.dest(outputFiles + 'css/'));
});

gulp.task('default', async function () {
    console.log(chalk.keyword('orange')("Vous n'avez pas renseigné de tache,je vous conseille gulp build"));
    console.log();
    console.log();
    console.log();

});

gulp.task('watch', function () {
    gulp.watch(inputFiles + 'css/*.css', gulp.series('minifyCSS'));
    gulp.watch(inputFiles + 'js/*.js', gulp.series('minifyJS'));
});


gulp.task('buildAssetsJS', function () {
    return gulp.src([
        'node_modules/bootstrap/dist/js/bootstrap.js',
    ])
        .pipe(plugins.concat('assets.min.js'))
        .pipe(gulp.dest(outputFiles + 'js/'));
});

gulp.task('buildAssetsCSS', function () {
    return gulp.src([
        'node_modules/bootstrap/dist/css/bootstrap.css',
        'node_modules/chart.js/dist/Chart.bundle.js',
        'node_modules/jquery/dist/jquery.js',
    ])
        .pipe(plugins.less())
        .pipe(plugins.autoprefixer())
        .pipe(plugins.concat('assets.min.css'))
        .pipe(gulp.dest(outputFiles + 'css/'));
});

exports.minify = series('minifyCSS', 'minifyJS');
exports.watch = 'watch';
exports.buildAssets = series('buildAssetsCSS', 'buildAssetsJS');

exports.build = series(exports.minify /*, exports.buildAssets ,*/, exports.watch);