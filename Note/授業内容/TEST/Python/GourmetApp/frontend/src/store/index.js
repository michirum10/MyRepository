// src/store/index.js
import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
    // アプリケーションの状態をここに定義します
    restaurants: [],
    favoriteRestaurants: []
    },
    mutations: {
        // 状態を変更するためのミューテーションをここに定義します
        SET_RESTAURANTS(state, restaurants) {
        state.restaurants = restaurants;
        },
        ADD_FAVORITE(state, restaurant) {
        state.favoriteRestaurants.push(restaurant);
        }
    },
    actions: {
        // ミューテーションを呼び出すためのアクションをここに定義します
        fetchRestaurants({ commit }) {
        // 例: API からデータを取得する処理
        fetch('/api/restaurants')
            .then(response => response.json())
            .then(data => {
            commit('SET_RESTAURANTS', data);
            });
        },
        addFavorite({ commit }, restaurant) {
        commit('ADD_FAVORITE', restaurant);
        }
    },
    getters: {
        // 状態からデータを取得するためのゲッターをここに定義します
        allRestaurants(state) {
        return state.restaurants;
        },
        favoriteRestaurants(state) {
        return state.favoriteRestaurants;
        }
    }
    });
