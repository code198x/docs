# Enable the Code198x Cloudflare proxy

Scope: proxy `code198x.com` and `www.code198x.com`, retaining GitHub Pages hosting and deployment. The live homepage has no analytics beacon because Web Analytics automatic installation is enabled while all website DNS records are DNS-only.

## Steps

1. Inspect the nine website DNS records, origin HTTPS, Cloudflare edge certificate and Web Analytics rules. Verify the edge certificate covers both hostnames and origin HTTPS succeeds.
2. Set the zone TLS mode from Full to Full (strict), then patch only `proxied` to `true` on the four apex A records, four apex AAAA records and www CNAME. Verify API readback preserves record values and unrelated records.
3. Check authoritative DNS, live HTTPS, the www redirect, representative site assets and automatic beacon injection. Use a browser to check beacon delivery when available. Distinguish successful collection requests from dashboard reporting.
4. Record the resulting configuration and evidence in `website.md`, then commit and push only this task's documentation.

The user also approved including UK/EU visitors. Set the existing Web Analytics
site to `lite: false`, retaining automatic installation and its existing rule.

## Recovery

If the proxy causes delivery failures, set these nine records back to `proxied: false`. Restore TLS mode to `full` if reverting the complete change. Do not change DNS targets, mail records, hosting or deployment workflows. Keep existing analytics collection rules unless a change is needed and authorised.

## Files

- `plans/2026-10-13-cloudflare-proxy.md`: execution plan.
- `website.md`: hosting and analytics operating guidance after verification.
