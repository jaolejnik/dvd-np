import commentService from "@/services/commentService";

const state = {
    comments: [],
};

const getters = {
    comments: (state) => {
        return state.comments;
    },
};

const actions = {
    getComments({ commit }) {
        commentService.fetchComments().then((comments) => {
            commit("setComments", comments);
        });
    },

    addComment({ commit }, comment) {
        commentService.postComment(comment).then(() => {
            commit("addComment", comment);
        });
    },

    deleteComment({ commit }, commentID) {
        commentService.deleteComment(commentID).then(() => {
            commit("deleteComment", commentID);
        });
    },
};

const mutations = {
    setComments(state, comments) {
        state.comments = comments;
    },

    addComment(state, comment) {
        state.comments.push(comment);
    },

    deleteComment(state, commentID) {
        state.comments = state.comments.filter((obj) => obj.id !== commentID);
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
};
