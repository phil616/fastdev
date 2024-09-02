import Cookies from "js-cookie";
import {jwtDecode} from "jwt-decode"; // jwt-decode is required to decode the token

function checkAuthorizaion() {
    console.log("Checking authorization");
    const token = Cookies.get("token");
    if (token) {
        try {
            const decodedToken = jwtDecode(token);
            const currentTime = Date.now() / 1000;
            if (decodedToken.exp > currentTime) {
                sessionStorage.setItem("token", token);
                return true;
            } else {
                return false;
            }
        } catch (error) {
            error;
            // token is invalid or expired
            return false;
        }
    } else {
        return false;
    }
}

function loadSessionToken() {
    const token = sessionStorage.getItem("token");
    if (token) {
        return token;
    } else {
        return null;
    }
}

function logout() {
    Cookies.remove("username");
    Cookies.remove("token");
    sessionStorage.removeItem("token");
}

export { checkAuthorizaion, logout, loadSessionToken };