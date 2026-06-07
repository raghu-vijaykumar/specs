# Localization (i18n)

Internationalization patterns for mobile apps: string extraction, locale fallback, RTL, dynamic text sizing, and validation.

---

## 1. Principles

- **i18n from day one** — add localization infrastructure before the first user-facing string. Retrofitting is costly and error-prone.
- **Never concatenate strings** — use interpolation/formatting parameters. Concatenation breaks word order in other languages.
- **One source of truth** — all strings live in a single canonical file per platform:
  - Flutter: `.arb` (Application Resource Bundle)
  - Android: `strings.xml` in `res/values/`
  - iOS: `Localizable.strings` per locale
  - React Native: `.json` key-value files per locale
- **Canonical language is English** — all keys are defined in English first. Translations map from English to target locales.

---

## 2. String Extraction

### Key Naming Convention

```
{domain}_{context}_{purpose}
```

| Pattern | Example |
|---------|---------|
| `{screen}_{element}` | `settings_title`, `profile_email_label` |
| `{feature}_{action}_{state}` | `auth_login_error`, `checkout_payment_processing` |
| `{component}_{part}` | `card_title`, `button_loading_label` |

Rules:
- snake_case throughout
- Dots for deeper nesting: `auth.login.title`, `auth.login.error.invalid_email`
- Max 3 levels deep — deeper means the key structure should be refactored

### Interpolation

```
# Good
"welcome_message": "Hello, {name}! You have {count} notifications."

# Bad — never do this
"welcome_message": "Hello, " + name + "! You have " + count + " notifications."
```

### Comments for Translators

```xml
<!-- Android: strings.xml -->
<string name="auth_login_title">Sign in</string>
<!-- translators: max 30 chars, appears on the login button -->
```

```arb
{
  "@auth_login_title": {
    "description": "Login button label. Max 30 chars.",
    "source_text": "Sign in"
  }
}
```

---

## 3. Locale Handling

### Detection Priority

1. **User override** — explicit selection in settings (persisted)
2. **Device locale** — system language setting
3. **App default** — `en` (English)

### Fallback Chain

If a key is missing in the target locale, walk up the chain:

```
es-MX → es → en → key (show raw key as last resort)
```

- Never crash on a missing key — show the key itself (e.g., `[auth_login_title]`) or fall back to English.
- Every missing key is logged in debug mode.

### Locale Codes

- Use BCP 47 tags: `en`, `en-US`, `es`, `es-MX`, `fr`, `fr-CA`, `ja`, `ar`, `zh-Hans`, `zh-Hant`
- Android uses `values-b+es+MX` for `es-MX`; iOS uses `es-MX.lproj`

---

## 4. Pluralization & Formatting

### Plural Rules

Use ICU MessageFormat or platform equivalents:

```arb
{
  "notifications_count": "{count, plural, =0{No notifications} one{1 notification} other{{count} notifications}}"
}
```

| Platform | Mechanism |
|----------|-----------|
| Flutter | `intl` / ARB with `plural` |
| Android | `quantity strings` in `strings.xml` (`zero`, `one`, `two`, `few`, `many`, `other`) |
| iOS | `.stringsdict` with `NSStringPluralRuleType` |
| RN / JS | `intl-messageformat` / `react-intl` `FormattedPlural` |

### Number / Date / Currency

| Type | Rule | Example |
|------|------|---------|
| Number | Locale-appropriate grouping | `1,234.56` (en) vs `1.234,56` (de) |
| Date | `short`/`medium`/`long` per context | `Jun 7, 2026` vs `07/06/2026` |
| Time | 12h vs 24h per locale | `3:45 PM` (en) vs `15:45` (de) |
| Currency | Symbol position + spacing locale-dependent | `$1.99` (en) vs `1,99 €` (de) |
| Timezone | Always display in user's timezone; store in UTC | — |

- Never hardcode format strings — use the platform's locale-aware formatters.

### Measurement Units

- Use locale-preferred units: `mi` vs `km`, `°F` vs `°C`
- For imperial/metric, prefer the device locale default with an optional manual toggle in settings

---

## 5. RTL Layout

### Rules

- **No `left`/`right`** — use `start`/`end` for alignment, padding, and margins.
- **Mirroring** — entire screens mirror, not individual components. Exceptions (non-mirroring elements):
  - Numbers and phone numbers
  - Logos and brand marks
  - Media playback controls (rewind/forward icons)
  - Charts with fixed axis direction
- **Text direction** — bidirectional text: LTR runs embedded in RTL text auto-detect by the platform (Unicode Bidi Algorithm).
- **Custom painting** — manually mirror any `CustomPainter` or animation that uses fixed x-coordinates.

### Testing RTL

- Enable "Force RTL" in developer settings on both platforms
- Visual check: every screen renders without clipping or broken layouts
- Scroll direction reverses (content starts from right)
- Back gesture direction reverses (swipe right-to-left to go back on iOS)

### Platform Implementation

| Platform | RTL Entry |
|----------|-----------|
| Flutter | `Directionality` widget or `MaterialApp(theme: ThemeData(..., useMaterial3: true))` |
| Android | `android:supportsRtl="true"` in manifest |
| iOS | `UIApplication.shared.userInterfaceLayoutDirection` |
| RN | `I18nManager.forceRTL(true)` |

---

## 6. Dynamic Sizing

### Text Expansion Factors

| Language | Approx. expansion from English |
|----------|-------------------------------|
| German | +30% |
| Finnish | +40% |
| Russian | +30% |
| French | +20% |
| Spanish | +20% |
| Arabic | +25% |
| Japanese | -50% (shorter, but denser) |
| Korean | -40% |

### UI Resilience Rules

- **No fixed-width labels** — buttons, chips, and text fields resize to fit content with padding.
- **Truncation vs wrapping**:
  - Truncate with ellipsis: single-line titles, navigation items, bottom tab labels
  - Wrap: body text, descriptions, error messages, alerts, dialog content
  - No truncation: legal text, terms of service
- **Wrapping strategy** — prefer word-wrap over character-wrap. Hyphenation where the platform supports it.
- **Button min width** — set a `min-width` but not a `max-width`. German "Bezahlvorgang läuft" needs room.
- **Vertical expansion** — text fields and list rows grow vertically, never horizontally clip.
- **Layout baseline** — design at the widest anticipated locale (usually German or Finnish), then verify all others fit.

### Dynamic Type / Font Scaling

- Respect system font size settings (`Accessibility > Display & Text Size` on iOS, `Display > Font size` on Android).
- Test at all accessibility font sizes — ensure no text truncation at maximum size.
- Use `ScaleFactor` or `textScaleFactor` to cap max scaling only if the layout breaks (document the cap with a rationale in comments).

---

## 7. Testing & Validation

| Layer | Scope | Tool | Command | Failure |
|-------|-------|------|---------|---------|
| Unit | Missing key detection, fallback chain | Language test framework | `npm test` | Any key returns key name or empty string in non-debug mode |
| Pseudo-locale | UI breakage from text expansion | Platform pseudo-locale | Flutter: `flutter run --locale=en-XA` | Any text clipped or truncated |
| RTL | Layout mirroring correctness | Force RTL dev setting | Visual review | Content misaligned or clipped |
| Lint | Raw string in code without i18n wrapper | Custom lint rule | `npm run lint` | `Text('raw')` found without `AppLocalizations` |
| Integration | Every locale renders all screens | Screenshot diff per locale | `npm run test:locales` | Any screenshot differs from baseline beyond tolerance |
| Store | All app store metadata translated | Manual checklist | Review per locale in App Store Connect / Play Console | Missing or auto-translated field |
| E2E | App runs without crash in every supported locale | Device farm / emulator matrix | `npm run test:e2e -- --locales=es,de,ar,ja` | Crash or ANR on launch |

### Self-Validation

```bash
npm run lint && npm test && npm run test:locales
```

### Pseudo-Locale Commands

```bash
# Flutter — enable pseudo-locales in MaterialApp
flutter run --locale=en-XA  # pseudo-accents
flutter run --locale=en-XB  # pseudo-bidi (RTL + reversed)

# Android — enable in developer settings or via command
adb shell setprop debug.locale en-XA

# iOS — edit scheme > Run > Arguments Passed On Launch: -AppleLocale en_XA
```
