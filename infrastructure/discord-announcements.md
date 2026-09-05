# Discord announcements

The website's `.github/workflows/deploy.yml` owns publication announcements. Both the release webhook and optional aggregate webhook are GitHub Actions secrets. Identical targets are deduplicated; absent secrets produce a notice and no post. Never put webhook URLs in source or logs.

1. Fetch the currently deployed RSS feed before replacing it.
2. Build the new site and compare feeds with `scripts/discord-new-items.py`.
3. Prepare messages using `scripts/discord-payloads.py`; retain `new-items.json` and `discord-payloads.json` in the `new-items` artifact.
4. Deploy successfully, then post the prepared messages.

RSS supplies absolute URLs. Preserve them; resolve relative paths against the site origin rather than prefixing an origin unconditionally. Validate the messages before deployment. Batches respect both ten embeds and the combined 6,000-character limit; the implementation counts UTF-16 code units conservatively. Individual fields are shortened for readable announcements. See [Discord's embed limits](https://docs.discord.com/developers/resources/message#embed-limits).

Five messages per deployment remain the catch-up ceiling. Excess items produce a warning with the omitted count and remain available in `new-items.json`; they are not automatically queued. Payload regression tests run in the deployment build and locally with `python3 -m unittest discover -s scripts -p 'test_discord_*.py'`.

## Recovery and evidence

This is a feed comparison, not a delivery ledger. A later deployment does not automatically resend announcements that failed after the earlier deployment succeeded. The workflow retains the artifact for seven days. Download it promptly when investigating a failure.

Inspect delivery in each channel before retrying: a partially successful job may have posted some messages, and a retry can duplicate those. Ordinary transient HTTP failures receive bounded retries; a malformed-request response should be fixed rather than retried repeatedly. Keep any manual recovery scoped to the missing messages and channels. An offline payload test proves request construction, not delivery to Discord.

For failures from a workflow version before the fix, rerunning that old workflow still runs its old code. Use the retained item list with the corrected payload builder and review the resulting messages before an authorised recovery post.
