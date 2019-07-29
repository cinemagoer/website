lektor-gulp
===========

This plugin for `Lektor CMS`_ adds `gulp`_ support to projects. When
enabled with the ``-f gulp`` flag it runs ``npm install`` and then the
gulp ``default`` or ``watch`` tasks as they are defined into your own
``gulpfile.js``.

The general documentation about Lektor plugins is `here`_.

lektor build
------------

The command ``lektor build -f gulp`` runs the **``default``** gulp task,
for example defined as something like:

.. code::

   gulp.task('build', ['clean', 'copy', 'js', 'css', 'imagemin'], () => { });
   gulp.task('default', ['build'], () => { });

In the above example the ``default`` task points to a ``build`` task,
which is usually composed by several other gulp tasks, etc.

lektor server
-------------

The command ``lektor server -f gulp`` runs the Lektor embedded server on
http://localhost:5000, starting a gulp **``watch``** task in background.
For example, you can define something such as:

.. code::

   gulp.task('watch', () => {
       gulp.watch('lib/js/**/*.js', ['js']);
       gulp.watch('lib/css/**/*.css', ['css']);
   });

In the above example, each time one touches Javascript or CSS files in
the ``lib/`` folder then assets could be minified, concatenated and
copied into the standard ``assets/static/`` lektor folder, or whatever
is defined into your own ``gulpfile.js``.

Credits
-------

This plugin is based on the official `Webpack plugin`_ with very little
differences.

.. _Lektor CMS: https://www.getlektor.com
.. _gulp: http://gulpjs.com
.. _here: https://www.getlektor.com/docs/plugins/
.. _Webpack plugin: https://github.com/lektor/lektor-webpack-support