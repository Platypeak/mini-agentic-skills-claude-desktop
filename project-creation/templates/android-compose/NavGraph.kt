package {{PACKAGE_NAME}}.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import {{PACKAGE_NAME}}.screens.HomeScreen

sealed class Screen(val route: String) {
    object Home : Screen("home")
    // Add more screens here:
    // object Detail : Screen("detail/{id}")
}

@Composable
fun AppNavGraph() {
    val navController = rememberNavController()
    NavHost(navController = navController, startDestination = Screen.Home.route) {
        composable(Screen.Home.route) {
            HomeScreen(navController = navController)
        }
        // Register additional screens here
    }
}
