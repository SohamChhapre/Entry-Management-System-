import React from 'react';
import {Link} from 'react-router-dom';
import '../vistorform/style.css'
import axios from 'axios';
import config from '../../config/index'
class HostForm extends React.Component{
    constructor(){
        super();
        this.state={
            name:'',
            phone:'',
            email:'',
            errors:{}
        }
    }
    validate=()=>{
        const formattederrors={}
        let flag=true
        if (!this.state.email.includes('@')){
            formattederrors['email']="invalid email"
            flag=false
        }
        if (this.state.name.length<3){
          formattederrors['name']="Invalid name";
          flag=false
        }
        if (this.state.phone.length!==10){
          formattederrors['phone']="Please check phone no";
          flag=false
        }
        
        this.setState({
          errors:formattederrors
        })
        return flag;
      }
       handlesubmit=async (event)=>{
        
        event.preventDefault();
        const data = this.state;
        const isvalid=this.validate()
      
        if (isvalid){
           console.log(this.state);
           axios.post(`${config.apiUrl}/host`
           ,{name:this.state.name,
          email:this.state.email,
        phone_no:this.state.phone}
         )
         .then(response => {
             console.log("res"+response);
             console.log(response.data);
             
             this.props.history.push('/');
           })
           .catch( errors=>{
             console.log(errors)
           })
           
        }
        }
        
      handleInputChange=(event)=>{
         this.setState({
           [event.target.name] : event.target.value
         });
         console.log(this.state.name,this.state.email,this.state.phone);
      }
    render(){
        return(
            <form className="modal-content" onSubmit={this.handlesubmit}>
        <div className="container">
          <h1>Host Registeration Form</h1>
          <p>Please fill in this form to Register</p>
          <hr />
          <label htmlFor="email"><b>Email</b></label>
          <input type="email" placeholder="Enter Email" name="email" onChange={this.handleInputChange} required />
          { this.state.errors['email'] && <small className="text-danger" >{this.state.errors['email']}</small> }

          <label htmlFor="Name"><b>Name</b></label>
          <input type="text" placeholder="Enter Name" name="name" onChange={this.handleInputChange} required />
          { this.state.errors['name'] && <small className="text-danger" >{this.state.errors['name']}</small> }

          <label htmlFor="phoneno"><b>PhoneNumber</b></label>
          <input type="text" placeholder="Phone no" name="phone" onChange={this.handleInputChange} required />
          { this.state.errors['phone'] && <small className="text-danger" >{this.state.errors['phone']}</small> }

          <label>
           
          </label>
          
          <div className="clearfix">
            <Link type="button" to="/"  className="btn btn-danger mg">Cancel</Link>
            <button type="submit" className="btn btn-success mg">Register</button>
          </div>
        </div>
      </form>
        )
    }
}

export default HostForm;