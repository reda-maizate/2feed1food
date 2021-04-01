const gulp = require("gulp");
const { series } = require('gulp');
const plugins = require('gulp-load-plugins')();

const inputFiles = './project/static/';
const outputFiles = './project/dist/assets/';


gulp.task('minifyJS' ,function(){
    return gulp.src(inputFiles + 'js/*.js')
        .pipe(plugins.uglify())
        .pipe(plugins.concat('app.min.js'))
        .pipe(gulp.dest(outputFiles + 'js/'));
});

gulp.task('minifyCSS' , function (){
    return gulp.src(inputFiles + 'css/*.css')
        .pipe(plugins.less())
        .pipe(plugins.autoprefixer())
        .pipe(plugins.concat('app.min.css'))
        .pipe(gulp.dest(outputFiles + 'css/'));
});

gulp.task('noTaskGiven',function (){
    console.log("Vous n'avez pas renseigné de tache,je vous conseille gulp build");
});

gulp.task('watch', function() {
    gulp.watch(inputFiles + 'css/*.css', gulp.series('minifyCSS'));
    gulp.watch(inputFiles + 'js/*.js', gulp.series('minifyJS'));
});


exports.default = 'noTaskGiven';
exports.minify = series('minifyCSS','minifyJS');
exports.watch = 'watch';

exports.build = series(exports.minify , exports.watch);