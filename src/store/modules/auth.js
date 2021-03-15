// import api from '../../api/BackEnd';
// import {router} from '../../main';

const state = {
  dummy: true
};

const getters = {
  isTrue: state => !!state.dummy
};

const actions = {
  dummyMethod({commit},value) {
    commit('setDummy',value);
  }
};

const mutations = {
  setDummy(state,value) {
    state.dummy = value;
  }
};

export default {
  state,
  getters,
  actions,
  mutations
}
