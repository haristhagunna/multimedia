#!/bin/bash
# usage: tools/sync_push.sh "commit message"  (copies the site into the GitHub clone and pushes)
set -e
MSG="$1"
cd /home/claude/multimedia-site && git add -A >/dev/null && git commit -qm "$MSG" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011v58iHSMtZ3eFrJV4yVdsn" || true
cd /home/claude/multimedia && find . -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
(cd /home/claude/multimedia-site && tar --exclude=.git --exclude=site --exclude=tools/.mmcache --exclude=__pycache__ -cf - .) | tar -xf -
git add -A && git commit -qm "$MSG" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011v58iHSMtZ3eFrJV4yVdsn" || true
git push origin main 2>&1 | tail -1
