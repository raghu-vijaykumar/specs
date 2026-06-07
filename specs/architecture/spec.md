# Architecture

How the UI components, data, navigation, and project structure fit together. Framework-agnostic at the pattern level, with Flutter-specific notes.

---

## 1. Project Structure

### Folder Layout

```
lib/
  main.dart                        # App entry point, provider setup, theme wiring
  app/
    app.dart                       # MaterialApp widget, theme, router
    router.dart                    # Navigation graph (GoRouter or similar)
    theme/
      tokens.dart                  # Generated from specs/tokens.md
      app_theme.dart               # ThemeExtension, light/dark constructors
  features/                        # One folder per feature/screen
    auth/
      screens/
        login_screen.dart
        signup_screen.dart
      widgets/                     # Feature-specific widgets (not reusable)
        auth_header.dart
    profile/
      screens/
        profile_screen.dart
        edit_profile_screen.dart
      widgets/
    settings/
      screens/
        settings_screen.dart
      widgets/
    home/
      screens/
        home_screen.dart
      widgets/
  shared/                          # Reusable across features
    widgets/                       # Copied from spec implementation
      cards/
      inputs/
      buttons/
      navigation/
      feedback/
    models/                        # Data models (User, Product, etc.)
    services/                      # API client, auth service, storage
    utils/                         # Extensions, helpers, constants
  gen/                             # Code-generated files (tokens, assets)
    tokens.g.dart
    assets.g.dart
```

### Naming Conventions

| Thing | Convention | Example |
|-------|-----------|---------|
| File | `snake_case` | `login_screen.dart` |
| Class | `PascalCase` | `LoginScreen` |
| Widget method | `camelCase` | `buildHeader()` |
| Private | `_` prefix | `_LoginState` |
| Const | `camelCase` | `defaultPadding` |
| Token class | `camelCase` | `AppColors`, `AppSpacing` |

### What goes where

- **`features/`**: One folder per feature or screen. Screens, feature-specific widgets, and feature-specific services.
- **`shared/widgets/`**: Copied from specs. Reusable across features. No business logic.
- **`shared/services/`**: API, auth, storage. One class per concern.
- **`app/`**: App-wide setup. Theme, router, providers.

---

## 2. Screen Templates

Patterns for composing components into full screens. Every screen follows one of these templates.

### Feed / List Screen

```
┌─────────────────────────┐
│ App Bar (title, action)  │
├─────────────────────────┤
│ Search Bar + Filters    │  ← inputs/search + chips
├─────────────────────────┤
│                         │
│  ┌───┐  ┌───┐  ┌───┐   │
│  │ C │  │ C │  │ C │   │  ← cards in a grid or list
│  └───┘  └───┘  └───┘   │
│                         │
│ Floating Action Row     │  ← bottom sheets/floating row
└─────────────────────────┘
│ Bottom Navigation       │  ← navigation/bottom nav
└─────────────────────────┘
```

### Detail Screen

```
┌─────────────────────────┐
│ Back  Title      Action │  ← app bar with back
├─────────────────────────┤
│                         │
│   Media / Image         │  ← media/image viewer
│                         │
│   Title (h1)            │
│   Metadata line         │
│                         │
│   Body text...          │  ← scrollable content
│                         │
│   Action Card           │  ← cards/action card (sticky bottom)
│                         │
└─────────────────────────┘
```

### Form Screen

```
┌─────────────────────────┐
│ Cancel        Save      │  ← app bar
├─────────────────────────┤
│                         │
│    Text Field           │  ← inputs/text
│    Text Field           │
│    Date Picker          │  ← pickers/date
│    Toggle               │  ← inputs/toggle
│    Segmented Control    │  ← inputs/segmented
│                         │
│  ┌─────────────────┐    │
│  │    Primary       │    │  ← buttons/primary
│  └─────────────────┘    │
└─────────────────────────┘
```

### Settings Screen

```
┌─────────────────────────┐
│ Settings                │  ← app bar
├─────────────────────────┤
│ Section Header          │  ← lists/grouped
│ ┌─────────────────────┐ │
│ │ Row Item    >       │ │  ← lists/row
│ │ Row Item   Toggle   │ │
│ │ Row Item    >       │ │
│ └─────────────────────┘ │
│ Section Header          │
│ ┌─────────────────────┐ │
│ │ Row Item    >       │ │
│ └─────────────────────┘ │
└─────────────────────────┘
```

### Auth Screen

```
┌─────────────────────────┐
│                         │
│      App Logo           │  ← centered branding
│     (80px icon)         │
│                         │
│      Welcome            │  ← type.display
│      Tagline            │  ← type.body textMuted
│                         │
│  ┌─────────────────┐    │
│  │    Text Field    │    │  ← inputs/text
│  └─────────────────┘    │
│  ┌─────────────────┐    │
│  │    Text Field    │    │
│  └─────────────────┘    │
│                         │
│  ┌─────────────────┐    │
│  │   Sign In        │    │  ← buttons/primary
│  └─────────────────┘    │
│                         │
│     Create Account      │  ← buttons/ghost
│     Forgot Password?    │
│                         │
└─────────────────────────┘
```

---

## 3. Navigation Map

The screen graph. Every app follows this general shape.

### Auth Flow (not logged in)

```
Splash → Onboarding → Login/Signup → Main Flow
                         ↑______________|
                      (logout)
```

- Splash checks auth state → routes accordingly
- Onboarding shown once (local flag)
- Login/Signup are full-screen, no bottom nav

### Main Flow (logged in)

```
                    Main Shell (BottomNav)
                    ┌──────────────────────┐
                    │ Tab 1   Tab 2   Tab 3 │
                    └──────┬───────┬───────┘
                           │       │
              ┌────────────┘       └────────────┐
              ↓                                  ↓
         Home Screen                       Settings Screen
              │                                  │
              ↓                                  ↓
         Detail Screen                     About Screen
              │                             Legal Pages
              ↓
         (Modal sheet)
```

### Modal / Overlay Routes
- **Bottom sheets**: presented modally on any screen
- **Dialogs**: presented modally on any screen
- **Full-screen modal**: Login (from settings), Image viewer, Force update

### Deep Links

| URL | Routes to |
|-----|-----------|
| `yourapp://profile/{id}` | Profile detail screen |
| `yourapp://settings` | Settings screen |
| `yourapp://legal/privacy` | Privacy policy (in-app browser or screen) |

- Push notifications carry a `route` payload → navigate on tap
- All deep links require auth check first

---

## 4. Data Flow

Every screen follows the same state machine.

### Screen State Machine

```
          ┌──────────┐
          │  Initial  │
          └────┬─────┘
               ↓
          ┌──────────┐    ┌──────────┐
          │  Loading  │───→│  Empty   │  (no data)
          └────┬─────┘    └──────────┘
               ↓
          ┌──────────┐    ┌──────────┐
          │  Success  │───→│  Error   │  (retry → Loading)
          └──────────┘    └──────────┘
               │
               ↓
          ┌──────────┐
          │  Refresh  │  (pull-to-refresh, silent reload)
          └──────────┘
```

- **Loading**: skeleton loader (`specs/feedback`)
- **Empty**: empty state (`specs/feedback`)
- **Error**: error state with retry (`specs/feedback`)
- **Success**: the actual content
- **Refresh**: existing content stays visible, loading indicator at top

### API Layer Pattern

```
UI (Screen/Widget)
    │  calls
    ↓
Repository (caching, offline logic)
    │  calls
    ↓
ApiClient (HTTP, auth headers, error mapping)
    │  calls
    ↓
Network (dio/http package)
```

- **Repository**: decides cache-first vs network-first per endpoint
- **ApiClient**: adds auth token, maps 401 → logout, maps 5xx → error
- **Mutation** (create/update/delete): optimistic update + rollback on failure

### Local Storage
- Auth tokens: secure storage (flutter_secure_storage)
- User preferences: shared_preferences or similar
- Offline queue: local database (drift, hive, or sqflite)

---

## 5. Error Handling

### Global Error Boundary

A single widget wraps the app and catches unhandled exceptions:

```
AppErrorBoundary
  ↓ catches
  ↓
Shows generic error screen with "Something went wrong"
  ↓
Option to "Restart" (rebuild app state)
```

### Network Errors

| Error | Where it shows | Action |
|-------|---------------|--------|
| No connection | Offline banner at top of screen | Auto-hides when connection returns |
| 401 Unauthorized | Redirect to login | Clear auth state |
| 403 Forbidden | Toast "You don't have access" | None |
| 404 Not Found | Empty state "Not found" | Go back |
| 422 Validation | Inline error on the relevant field | Fix input |
| 500+ Server Error | Error state with retry button | Retry |
| Timeout | Toast "Request timed out" | Retry |

### Offline Detection
- Monitor connectivity changes
- Show a persistent banner: "You're offline. Some features may be limited."
- Queue mutations for when connectivity returns
- Read from cache while offline

---

## 6. Build Pipeline

How tokens flow from `specs/tokens.md` into generated Dart code.

### Token Generation

```
specs/tokens.md
      │
      │ (manual or code-gen script)
      ↓
lib/gen/tokens.g.dart
```

The generated file exports:
```dart
class AppColors {
  static const light = AppColorSet(/* from tokens.md Light column */);
  static const dark  = AppColorSet(/* from tokens.md Dark column */);
}
class AppSpacing { ... }
class AppRadius { ... }
class AppTypography { ... }
class AppShadows { ... }
```

Two approaches:

| Approach | When to use |
|----------|-------------|
| **Manual copy** | Small apps, fast iteration. Copy values by hand when tokens change. |
| **Code generation** | Larger apps. A short script reads `tokens.md` and writes `tokens.g.dart`. Run on every token change. |

### Theme Injection

```
main.dart
  │
  ├── AppTheme.light()  ⇦ reads AppColors.light, AppSpacing, etc.
  └── AppTheme.dark()   ⇦ reads AppColors.dark
         │
         ↓
  ThemeData.extensions = [AppTheme.light()]
         │
         ↓
  Widget builds → Theme.of(context).extension<AppTheme>()!.colors.primary
```

- `AppTheme` is a `ThemeExtension` (Flutter's built-in system for custom theme tokens)
- Every widget reads tokens through `Theme.of(context).extension<AppTheme>()`
- No widget imports `tokens.g.dart` directly — they always go through the theme
- This preserves hot reload and allows runtime theme switching

### Dark/Light Toggle Flow
```
User taps toggle
  → setState(() => _isDark = !_isDark)
  → MaterialApp rebuilds with darkTheme/theme
  → all Theme.of(context).extension<AppTheme>() resolves to the new mode
  → all widgets re-render with new colors
```

System mode: remove the manual toggle, let `MediaQuery.platformBrightness` drive the selection.
