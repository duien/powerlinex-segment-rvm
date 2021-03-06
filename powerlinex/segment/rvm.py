from __future__ import absolute_import
from subprocess import Popen, PIPE
from powerline.theme import requires_segment_info


def readlines(cmd, cwd):
    p = Popen(cmd, shell=False, stdout=PIPE, stderr=PIPE, cwd=cwd)
    p.stderr.close()
    with p.stdout:
        for line in p.stdout:
            yield line[:-1].decode('utf-8')


@requires_segment_info
def version(pl, segment_info):
    try:
      for line in readlines(["rvm-prompt", "i v g"], segment_info['getcwd']()):
          # Now to process line
          if line == "system":
              return None
          else:
              # ret = []
              # info = line.split('@')
              # if len(info) > 1:
              #     ret.append({
              #         'contents': info[1],
              #         'highlight_group': ['ruby_version', 'virtualenv']
              #     })
              # version = info[0]
              # info = version.split('-', 1)
              # if info[0] == 'ruby':
              #     ret.insert(0, {
              #         'contents': info[1],
              #         'highlight_group': ['ruby_version', 'virtualenv']
              #     })
              # else:
              #     ret.prepend({
              #         'contents': version,
              #         'highlight_group': ['ruby_version', 'virtualenv']
              #     })
              # return ret
              return [{
                  'contents': line,
                  'highlight_group': ['ruby_version', 'virtualenv']
              }]
    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
