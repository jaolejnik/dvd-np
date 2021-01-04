import api from "@/services/api";

export default {
    fetchComments() {
        return api.get(`comments/`).then((response) => response.data);
    },

    postComment(payload) {
        return api.post(`comments/`, payload).then((response) => response.data);
    },

    deleteComment(commentID) {
        return api.delete(`comments/${commentID}/`).then((response) => response.data);
    },
};
