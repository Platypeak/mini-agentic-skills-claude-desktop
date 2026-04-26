# Template: Android Jetpack Compose

## What This Provides
| File | Purpose |
|---|---|
| `app/build.gradle.kts` | App-level Gradle with Compose dependencies |
| `build.gradle.kts` | Project-level Gradle |
| `settings.gradle.kts` | Project settings |
| `gradle.properties` | Compose compiler flags |
| `app/src/main/AndroidManifest.xml` | App manifest |
| `app/src/main/java/.../MainActivity.kt` | Entry activity with NavHost |
| `app/src/main/java/.../ui/theme/Theme.kt` | Material3 theme setup |
| `app/src/main/java/.../ui/theme/Color.kt` | Color palette |
| `app/src/main/java/.../navigation/NavGraph.kt` | Navigation graph scaffold |
| `app/src/main/java/.../screens/HomeScreen.kt` | Placeholder home screen |
| `.gitignore` | Android ignores |
| `README.md` | Setup instructions |

## Placeholders
| Placeholder | Replaced With |
|---|---|
| `{{PROJECT_NAME}}` | App name shown on device |
| `{{PACKAGE_NAME}}` | e.g. `com.rohan.myapp` |
| `{{DESCRIPTION}}` | One-line app description |
| `{{MIN_SDK}}` | Minimum SDK (default: 26) |
| `{{TARGET_SDK}}` | Target SDK (default: 35) |

## Manual Steps After Generation
1. Open in Android Studio (Hedgehog or newer)
2. Let Gradle sync complete
3. Set up an emulator or connect a device
4. Run the app via the green play button
5. Add your screens in `screens/` and register them in `NavGraph.kt`
