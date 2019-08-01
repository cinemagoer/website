# -*- coding: utf-8 -*-
import os

from lektor.pluginsystem import Plugin
from lektor.reporter import reporter
from lektor.utils import portable_popen


class GulpPlugin(Plugin):
    name = u'lektor-gulp'
    description = u'A simple Lektor plugin for gulp'

    def __init__(self, *args, **kwargs):
        Plugin.__init__(self, *args, **kwargs)
        self.gulp_process = None

    def is_enabled(self, extra_flags):
        return bool(extra_flags.get('gulp'))

    def npm_install(self):
        reporter.report_generic('Running npm install')
        gulp_root = os.path.join(self.env.root_path, '.')
        portable_popen(['npm', 'install'], cwd=gulp_root).wait()

    def run_gulp(self, task):
        gulp_root = os.path.join(self.env.root_path, '.')
        args = [os.path.join(gulp_root, 'node_modules', '.bin', 'gulp'), task]
        return portable_popen(args, cwd=gulp_root)

    def on_server_spawn(self, **extra):
        extra_flags = extra.get("extra_flags") or extra.get("build_flags") or {}
        if not self.is_enabled(extra_flags):
            return
        self.npm_install()
        reporter.report_generic('Spawning gulp watcher')
        self.gulp_process = self.run_gulp("watch")

    def on_server_stop(self, **extra):
        if self.gulp_process is not None:
            reporter.report_generic('Stopping gulp watcher')
            self.gulp_process.kill()
            self.run_gulp("after_build").wait()

    def on_before_build_all(self, builder, **extra):
        extra_flags = getattr(
            builder, "extra_flags", getattr(builder, "build_flags", None)
        )
        if not self.is_enabled(extra_flags) or self.gulp_process is not None:
            return
        self.npm_install()
        reporter.report_generic('Starting gulp build')
        self.run_gulp("build").wait()
        reporter.report_generic('Gulp build finished')

    def on_after_build_all(self, builder, **extra):
        extra_flags = getattr(
            builder, "extra_flags", getattr(builder, "build_flags", None)
        )
        if not self.is_enabled(extra_flags) or self.gulp_process is not None:
            return
        reporter.report_generic('Starting gulp build')
        self.run_gulp("after_build").wait()
        reporter.report_generic('Gulp build finished')

    def on_process_template_context(self, context, **extra):
        def test_function():
            return 'Value from plugin %s' % self.name
        context['test_function'] = test_function
