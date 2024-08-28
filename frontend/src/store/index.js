// store.js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        navigator_drawer: false,
        authenticated: false,
    },
    mutations: {
        set_navigator_drawer(state, value) {
            state.navigator_drawer = value
        },
        set_authenticated(state, value) {
            state.authenticated = value
        },
        toggle_navigator_drawer(state) {
            state.navigator_drawer =!state.navigator_drawer
        }
    },
    actions: {
        set_navigator_drawer({ commit }, value) {
            commit('set_navigator_drawer', value)
        },
        set_authenticated({ commit }, value) {
            commit('set_authenticated', value)
        },
        toggle_navigator_drawer({ commit }) {
            commit('toggle_navigator_drawer')
        }
    },
    getters: {
        get_navigator_drawer: state => state.navigator_drawer,
        get_authenticated: state => state.authenticated
    }
})