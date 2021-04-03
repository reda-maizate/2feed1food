const gulp = require("gulp");
const {series} = require('gulp');
const plugins = require('gulp-load-plugins')();
const chalk = require('chalk');
const plumber = require('gulp-plumber');
const eslint = require("gulp-eslint");

const inputFiles = './project/static/';
const outputFiles = './project/static/assets/';


gulp.task('minifyJS', function () {
    return gulp.src([
        inputFiles + 'js/*.js'
    ])
        .pipe(plumber())
        .pipe(plugins.concat('main.js'))
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
        'node_modules/chart.js/dist/Chart.js',
        'node_modules/jquery/dist/jquery.js',
        'node_modules/jquery-ui-dist/jquery-ui.js'
    ])
        .pipe(plugins.concat('assets.min.js'))
        .pipe(gulp.dest(outputFiles + 'js/'));
});

gulp.task('buildAssetsCSS', function () {
    return gulp.src([
        'node_modules/bootstrap/dist/css/bootstrap.css',
        'node_modules/jquery-ui-dist/jquery-ui.css',
        'node_modules/bootstrap-icons/font/bootstrap-icons.css',
    ])
        // .pipe(plugins.less())
        .pipe(plugins.autoprefixer())
        .pipe(plugins.concat('assets.min.css'))
        .pipe(gulp.dest(outputFiles + 'css/'));
});

gulp.task('buildAssetsFonts' , function(){
    return gulp.src([
        'node_modules/bootstrap-icons/font/fonts/bootstrap-icons.woff',
        'node_modules/bootstrap-icons/font/fonts/bootstrap-icons.woff2'
    ])
    .pipe(gulp.dest(outputFiles + 'css/fonts/'));
})

exports.minify = series('minifyCSS', 'minifyJS');
exports.watch = 'watch';
exports.buildAssets = series('buildAssetsCSS', 'buildAssetsJS' , 'buildAssetsFonts');

exports.build = series(exports.minify , exports.buildAssets , exports.watch);