# Legal & Compliance

Content pages and dialogs required by law, platform policy, or good citizenship. Every app needs these — the content differs, the layout pattern stays the same.

## Privacy Policy

### Layout
- Full-screen scrollable text page
- Title: `{type.h1}`, last updated date: `{type.caption}` `{color.textMuted}`
- Body: `{type.body}` `{color.text}`, 1.6 line height for readability
- Padding: `{space.lg}` sides, `{space.lg}` between sections
- Max content width: 600px (centered on tablets)

### Content Sections (template)
1. **Information We Collect** — account data, usage data, device info, location
2. **How We Use It** — service delivery, improvements, communications
3. **Data Sharing** — third parties, legal requirements, anonymized analytics
4. **Data Retention** — how long data is kept
5. **Your Rights** — access, correction, deletion, portability
6. **Children's Privacy** — age restrictions
7. **Changes** — how updates are communicated
8. **Contact** — email, address, DPO info

### Accessibility
- `{type.body}` at min 16px for readability
- Screen reader: `heading` hierarchy for sections
- Links in `{color.primary}` with underline

---

## Terms of Service

### Layout
- Same scrollable page layout as Privacy Policy
- Add a **"Accept"** button at bottom that sticks on scroll
- Button: primary, full width, `{space.lg}` margin from edges
- If not accepted, app shows this on first launch

### Content Sections (template)
1. **Acceptance** — using the app = agreeing to terms
2. **Account** — registration responsibility, security
3. **Acceptable Use** — prohibited behaviors
4. **Purchases & Subscriptions** — billing, refunds, auto-renewal
5. **Intellectual Property** — ownership of content
6. **Limitation of Liability** — disclaimers
7. **Termination** — account suspension
8. **Governing Law** — jurisdiction

### Entry Point
- Linked from: Sign-up screen, Settings → Legal, first launch
- Acceptance recorded as a boolean flag per user

---

## Licenses & Credits

### Layout
- Expandable list of libraries
- Each item: library name → expand to show full license text
- Grouped by: "Open Source Licenses", "Icons", "Fonts"
- Search bar at top for long lists

### Content Per Item
- Library name, author, license type (MIT, Apache 2.0, etc.)
- Full license text in scrollable area when expanded
- Link to source repository

### Entry Point
- Usually: Settings → About → Licenses
- Also shown on first launch for attribution requirements

---

## Cookie Consent

### Layout
- Bottom bar (not a sheet — persistent but low-profile)
- Text: `{type.bodySm}` "We use cookies to improve your experience."
- Two buttons: **Accept** (primary, compact) | **Settings** (ghost, compact)
- Bar: `{color.surface}`, top border `{color.border}`, padding `{space.lg}`

### Detail Modal (on "Settings")
- Standard modal sheet (`{radius.lg}`)
- List of cookie categories with toggles:
  - **Essential** (always on, no toggle) — auth, security
  - **Analytics** (toggle) — page views, crashes
  - **Marketing** (toggle) — ads, personalization
- Buttons: Save (primary), Accept All (ghost)

### Behavior
- Shown once per session until accepted
- Stored preference persists across app reinstalls (if signed in)
- Essential cookies cannot be disabled

### Accessibility
- Cookie bar: `status` role
- Toggles: `switch` role with labels

---

## Data Export & Account Deletion

### Layout
- Two separate flows, same pattern:
  1. **Export My Data** → trigger email with download link
  2. **Delete My Account** → confirmation flow → irreversible

### Delete Account Flow
1. Info screen: "This will permanently delete your account and data."
   - Bullet list of what gets deleted
   - Bullet list of what is retained (legal obligation)
2. Confirmation: type "DELETE" in a text field to confirm
3. Final button: red `{color.error}` → "Permanently Delete"
4. Success screen: "Account scheduled for deletion. You'll receive a confirmation email."

### Entry Point
- Settings → Privacy → Export Data / Delete Account
- GDPR/CCPA: accessible from account settings directly

### Accessibility
- Destructive action: `{color.error}` background, white text
- Confirmation text field: label "Type DELETE to confirm"
- Multiple warnings before final action

---

## Accessibility Statement

### Layout
- Scrollable text page (same as Privacy Policy)
- Lists conformance level (WCAG 2.1 AA recommended)
- Describes accessibility features of the app
- Provides contact for accessibility issues

### Content Sections
1. **Conformance Status** — partially conformant / fully conformant
2. **Accessibility Features** — text scaling, contrast, screen reader support
3. **Known Limitations** — areas being improved
4. **Feedback** — email/phone for accessibility issues

### Entry Point
- Settings → Accessibility → Accessibility Statement
- Link in app footer or legal section
