import axios from "axios";

const request = axios.create({
  baseURL: "/api",
});

const get = async (url: string) => {
  try {
    const response = await request.get(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

const post = async (url: string, data: any) => {
  try {
    const response = await request.post(url, data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

const put = async (url: string, data: any) => {
  try {
    const response = await request.put(url, data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

const del = async (url: string) => {
  try {
    const response = await request.delete(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export default { get, post, put, del };
